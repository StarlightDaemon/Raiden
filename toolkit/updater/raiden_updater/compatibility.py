"""Schema and version compatibility checks.

The current updater contract treats ``compatible_instance_schemas`` as a
simple set-membership check against the instance schema version.
"""

from __future__ import annotations

from .models import InstanceMetadata, PackageManifest


def check_schema_compatibility(
    metadata: InstanceMetadata,
    manifest: PackageManifest,
) -> tuple[bool, str]:
    """Check whether the package is compatible with the instance schema.

    Returns ``(compatible, detail)`` where *detail* explains the result.
    """
    instance_schema = metadata.instance_schema_version
    compatible_schemas = manifest.compatible_instance_schemas

    if instance_schema in compatible_schemas:
        return True, (
            f"Instance schema {instance_schema!r} is in the package's "
            f"compatible set {compatible_schemas}"
        )

    return False, (
        f"Instance schema {instance_schema!r} is NOT in the package's "
        f"compatible set {compatible_schemas}"
    )
