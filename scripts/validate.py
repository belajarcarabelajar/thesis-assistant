"""Repository checks for the thesis-assistant marketplace (run in CI and locally).

  uv run --with pyyaml python scripts/validate.py

Checks: marketplace.json and every plugin.json parse; each marketplace source exists and its
plugin.json name matches; the root and each plugin ship an Apache 2.0 LICENSE and a NOTICE;
every SKILL.md has YAML frontmatter whose name equals its folder and a real description.
Exits 1 on any finding.
"""
import json, pathlib, sys
import yaml

root = pathlib.Path(__file__).resolve().parent.parent
problems = []

def apache(path):
    t = path.read_text(encoding="utf-8") if path.is_file() else ""
    return "Apache License" in t and "Version 2.0" in t

if not apache(root / "LICENSE"):
    problems.append("LICENSE: missing or not Apache 2.0")
if not (root / "NOTICE").is_file():
    problems.append("NOTICE: missing")

try:
    market = json.loads((root / ".claude-plugin/marketplace.json").read_text(encoding="utf-8"))
except Exception as e:
    sys.exit(f"marketplace.json: {e}")

for entry in market.get("plugins", []):
    name, src = entry.get("name"), entry.get("source")
    pdir = (root / src).resolve() if isinstance(src, str) else None
    if pdir is None or not pdir.is_dir() or root not in pdir.parents:
        problems.append(f"{name}: source {src!r} is not a folder inside the repo")
        continue
    try:
        manifest = json.loads((pdir / ".claude-plugin/plugin.json").read_text(encoding="utf-8"))
        if manifest.get("name") != name:
            problems.append(f"{name}: plugin.json name is {manifest.get('name')!r}")
    except Exception as e:
        problems.append(f"{name}: plugin.json: {e}")
    if not apache(pdir / "LICENSE"):
        problems.append(f"{name}: LICENSE missing or not Apache 2.0")
    if not (pdir / "NOTICE").is_file():
        problems.append(f"{name}: NOTICE missing")
    skills = sorted(pdir.glob("skills/*/SKILL.md"))
    if not skills:
        problems.append(f"{name}: no skills found")
    for f in skills:
        label = f"{name}:{f.parent.name}"
        text = f.read_text(encoding="utf-8")
        parts = text.split("---\n")
        if not text.startswith("---\n") or len(parts) < 3:
            problems.append(f"{label}: no YAML frontmatter")
            continue
        try:
            fm = yaml.safe_load(parts[1])
        except yaml.YAMLError as e:
            problems.append(f"{label}: frontmatter is not valid YAML: {str(e).splitlines()[0]}")
            continue
        if not isinstance(fm, dict) or fm.get("name") != f.parent.name:
            problems.append(f"{label}: frontmatter name does not match the folder")
        elif len(str(fm.get("description", ""))) < 50:
            problems.append(f"{label}: description missing or too short")
        else:
            print(f"ok   {label}")

for p in problems:
    print(f"FAIL {p}")
sys.exit(1 if problems else 0)
