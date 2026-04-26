import json
from pathlib import Path
from http.server import HTTPServer
import threading
import urllib.request
import urllib.error

from raiden_updater.server import InstallerAPIHandler
from .conftest import SAMPLE_PACKAGE

def test_server_startup_and_endpoints(tmp_path: Path):
    """Test that the server handles endpoints correctly."""
    
    server = HTTPServer(("127.0.0.1", 0), InstallerAPIHandler)
    port = server.server_port
    
    thread = threading.Thread(target=server.serve_forever)
    thread.daemon = True
    thread.start()
    
    base_url = f"http://127.0.0.1:{port}"
    
    try:
        # Test 1: OPTIONS method
        req = urllib.request.Request(f"{base_url}/api/scan", method="OPTIONS")
        response = urllib.request.urlopen(req)
        assert response.status == 200
        assert response.getheader("Access-Control-Allow-Methods") == "GET, POST, OPTIONS"

        # Test 2: Missing body (400)
        req = urllib.request.Request(f"{base_url}/api/scan", method="POST")
        try:
            urllib.request.urlopen(req)
            assert False, "Should have thrown 400"
        except urllib.error.HTTPError as e:
            assert e.code == 400
            
        # Test 3: Scan legacy artifacts
        body = json.dumps({"instance_root": str(tmp_path)}).encode("utf-8")
        req = urllib.request.Request(f"{base_url}/api/scan", data=body, method="POST")
        req.add_header("Content-Type", "application/json")
        req.add_header("Content-Length", str(len(body)))
        response = urllib.request.urlopen(req)

        assert response.status == 200
        resp_data = json.loads(response.read().decode("utf-8"))
        assert "legacy_artifacts" in resp_data
        assert resp_data["legacy_artifacts"] == []
        assert resp_data["has_instance_root"] is False

        # Test 4: Preview initialization
        req = urllib.request.Request(f"{base_url}/api/init-preview", data=body, method="POST")
        req.add_header("Content-Type", "application/json")
        req.add_header("Content-Length", str(len(body)))
        response = urllib.request.urlopen(req)

        assert response.status == 200
        resp_data = json.loads(response.read().decode("utf-8"))
        assert "planned_writes" in resp_data
        assert any(item["path"] == "AGENTS.md" for item in resp_data["planned_writes"])

        # Test 5: Apply initialization
        req = urllib.request.Request(f"{base_url}/api/init-apply", data=body, method="POST")
        req.add_header("Content-Type", "application/json")
        req.add_header("Content-Length", str(len(body)))
        response = urllib.request.urlopen(req)

        assert response.status == 200
        resp_data = json.loads(response.read().decode("utf-8"))
        assert "written_paths" in resp_data
        assert (tmp_path / ".raiden" / "instance" / "metadata.json").exists()

        # Test 6: Plan after initialization
        plan_body = json.dumps({
            "instance_root": str(tmp_path),
            "package_root": str(SAMPLE_PACKAGE),
        }).encode("utf-8")
        req = urllib.request.Request(f"{base_url}/api/plan", data=plan_body, method="POST")
        req.add_header("Content-Type", "application/json")
        req.add_header("Content-Length", str(len(plan_body)))
        response = urllib.request.urlopen(req)

        assert response.status == 200
        resp_data = json.loads(response.read().decode("utf-8"))
        assert "file_actions" in resp_data
        assert "can_apply" in resp_data

        # Test 7: Doctor endpoint
        req = urllib.request.Request(f"{base_url}/api/doctor", data=body, method="POST")
        req.add_header("Content-Type", "application/json")
        req.add_header("Content-Length", str(len(body)))
        response = urllib.request.urlopen(req)

        assert response.status == 200
        resp_data = json.loads(response.read().decode("utf-8"))
        assert resp_data["ok"] is True

    finally:
        server.shutdown()
        thread.join(timeout=2)
