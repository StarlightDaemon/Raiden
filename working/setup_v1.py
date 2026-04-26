import os, json, hashlib
from pathlib import Path

payload_dir = Path('working/evaluation-package/v0.1.0/payload')
payload_dir.mkdir(parents=True, exist_ok=True)

files = {
    'README.md': '# Evaluation Package\nv0.1.0\n',
    'core_rules.md': '# Core Rules\nRule 1.\n',
    'templates/default.md': '# Default Template\nContent here.\n',
    'config/defaults.json': '{\n  "setting": "v0.1.0"\n}\n',
    'transient_cache.txt': 'This file will be removed in v0.2.0.\n'
}

for path, content in files.items():
    p = payload_dir / path
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(content, encoding='utf-8')

entries = []
for p in payload_dir.rglob('*'):
    if p.is_file():
        rel = p.relative_to(payload_dir).as_posix()
        h = hashlib.sha256(p.read_bytes()).hexdigest()
        entries.append({'path': rel, 'hash': h})

manifest = {
    'package_type': 'edict',
    'edict_version': '0.1.0',
    'compatible_instance_schemas': ['1'],
    'managed_files': entries,
    'created_at': '2026-04-24T21:00:00Z'
}

manifest_path = Path('working/evaluation-package/v0.1.0/manifest.json')
manifest_path.write_text(json.dumps(manifest, indent=2), encoding='utf-8')
print(f'Wrote v0.1.0 manifest with {len(entries)} files.')
