"""Local web HTTP server backend.

Provides a dependency-free JSON API for the RAIDEN local web installer/update
operator surface without duplicating planner or installer behavior.
"""

from __future__ import annotations

import dataclasses
import json
from http.server import BaseHTTPRequestHandler, HTTPServer
from pathlib import Path
from typing import Any
from urllib.parse import urlparse

from .applier import ApplyError, apply_plan
from .installer import (
    build_repo_scan,
    doctor,
    init_instance,
    preview_init_instance,
)
from .planner import create_plan


class InstallerAPIHandler(BaseHTTPRequestHandler):
    """Handles API requests for the RAIDEN local web installer."""

    def _send_json_response(self, status_code: int, data: dict[str, Any]) -> None:
        """Helper to send a JSON response."""
        self.send_response(status_code)
        self.send_header("Content-Type", "application/json")
        self.send_header("Access-Control-Allow-Origin", "*")  # Allow local UI cross-origin if needed
        self.end_headers()
        self.wfile.write(json.dumps(data).encode("utf-8"))

    def _send_error(self, status_code: int, message: str) -> None:
        """Helper to send an error response."""
        self._send_json_response(status_code, {"error": message})

    def _parse_json_body(self) -> dict[str, Any] | None:
        """Helper to parse a JSON request body."""
        content_length = int(self.headers.get("Content-Length", 0))
        if content_length == 0:
            return None
        body = self.rfile.read(content_length).decode("utf-8")
        try:
            return json.loads(body)
        except json.JSONDecodeError:
            return None

    def do_OPTIONS(self) -> None:
        """Handle CORS preflight requests."""
        self.send_response(200)
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.end_headers()

    def do_GET(self) -> None:
        """Handle GET requests."""
        self._send_error(405, "Method not allowed. Use POST for API requests")

    def do_POST(self) -> None:
        """Handle POST requests."""
        parsed_path = urlparse(self.path)
        body = self._parse_json_body()

        if body is None:
            self._send_error(400, "Invalid JSON body")
            return

        if parsed_path.path == "/api/scan":
            instance_root = self._require_instance_root(body)
            if instance_root is None:
                return
            result = build_repo_scan(instance_root)
            self._send_json_response(200, dataclasses.asdict(result))

        elif parsed_path.path == "/api/init-preview":
            instance_root = self._require_instance_root(body)
            if instance_root is None:
                return
            result = preview_init_instance(instance_root, force=bool(body.get("force", False)))
            self._send_json_response(200, dataclasses.asdict(result))

        elif parsed_path.path == "/api/init-apply":
            instance_root = self._require_instance_root(body)
            if instance_root is None:
                return
            instance_root.mkdir(parents=True, exist_ok=True)
            result = init_instance(instance_root, force=bool(body.get("force", False)))
            self._send_json_response(200, dataclasses.asdict(result))

        elif parsed_path.path == "/api/plan":
            instance_root = self._require_instance_root(body)
            if instance_root is None:
                return
            package_root_str = body.get("package_root")
            if not package_root_str:
                self._send_error(400, "Missing package_root")
                return
            package_root = Path(package_root_str)
            try:
                plan = create_plan(instance_root, package_root)
                self._send_json_response(200, dataclasses.asdict(plan))
            except Exception as e:
                self._send_error(500, f"Plan failed: {e}")

        elif parsed_path.path == "/api/apply":
            instance_root = self._require_instance_root(body)
            if instance_root is None:
                return
            package_root_str = body.get("package_root")
            if not package_root_str:
                self._send_error(400, "Missing package_root")
                return
            package_root = Path(package_root_str)
            try:
                plan = create_plan(instance_root, package_root)
                if not plan.can_apply:
                    self._send_error(400, f"Plan cannot be applied: {plan.block_reason}")
                    return

                apply_plan(plan, instance_root, package_root)
                self._send_json_response(200, {
                    "success": True,
                    "applied_version": plan.target_version,
                })
            except ApplyError as e:
                self._send_error(400, f"Apply failed: {e}")
            except Exception as e:
                self._send_error(500, f"Internal error during apply: {e}")

        elif parsed_path.path == "/api/doctor":
            instance_root = self._require_instance_root(body)
            if instance_root is None:
                return
            result = doctor(instance_root)
            self._send_json_response(200, dataclasses.asdict(result))

        elif parsed_path.path == "/api/select-folder":
            try:
                import tkinter as tk
                from tkinter import filedialog
            except ImportError:
                self._send_error(
                    503,
                    "tkinter not available in this environment, use manual path entry",
                )
                return

            root = tk.Tk()
            root.attributes("-topmost", True)
            root.withdraw()

            title = body.get("title", "Select Directory") if body else "Select Directory"
            selected_path = filedialog.askdirectory(title=title)

            root.destroy()

            self._send_json_response(200, {"path": selected_path or ""})

        else:
            self._send_error(404, "Not found")

    def _require_instance_root(self, body: dict[str, Any]) -> Path | None:
        """Extract and validate an instance root from the JSON body."""
        instance_root_str = body.get("instance_root")
        if not instance_root_str:
            self._send_error(400, "Missing instance_root")
            return None
        return Path(instance_root_str)


def serve(host: str = "127.0.0.1", port: int = 8080) -> None:
    """Start the local web API server."""
    server_address = (host, port)
    httpd = HTTPServer(server_address, InstallerAPIHandler)
    print(f"Starting RAIDEN local installer API on http://{host}:{port}")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        httpd.server_close()
        print("Server stopped.")

if __name__ == "__main__":
    serve()
