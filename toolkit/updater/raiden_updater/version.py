"""Semver-style version parsing and comparison.

Current updater canon uses strict core ``MAJOR.MINOR.PATCH`` versions with
three non-negative integer components. Prerelease and build metadata are not
part of the current supported version surface.
"""

from __future__ import annotations

from dataclasses import dataclass
import re


_CORE_VERSION_RE = re.compile(
    r"^(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)$"
)


@dataclass(frozen=True, order=True)
class Version:
    """Simple three-component version."""

    major: int
    minor: int
    patch: int

    def __str__(self) -> str:
        return f"{self.major}.{self.minor}.{self.patch}"


def parse_version(raw: str) -> Version:
    """Parse a ``MAJOR.MINOR.PATCH`` string into a Version.

    Raises ``ValueError`` on malformed input.
    """
    normalized = raw.strip()
    match = _CORE_VERSION_RE.fullmatch(normalized)
    if match is None:
        raise ValueError(
            f"Expected core MAJOR.MINOR.PATCH version, got {raw!r}"
        )
    return Version(
        int(match.group(1)),
        int(match.group(2)),
        int(match.group(3)),
    )


def compare_versions(current: str, target: str) -> str:
    """Compare two version strings.

    Returns one of ``"upgrade"``, ``"same"``, or ``"downgrade"``.
    """
    cur = parse_version(current)
    tgt = parse_version(target)
    if tgt > cur:
        return "upgrade"
    if tgt == cur:
        return "same"
    return "downgrade"
