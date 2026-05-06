#!/usr/bin/env python3
"""Validate data/*.json against schema and check links."""
import json
import sys
from pathlib import Path

try:
    import jsonschema
except ImportError:
    print("pip install jsonschema")
    sys.exit(1)

ROOT = Path(__file__).resolve().parents[2]
DATA = ROOT / "data"
SCHEMA_FILE = DATA / "schema.json"


def validate_schema():
    schema = json.loads(SCHEMA_FILE.read_text())
    errors = 0
    total = 0
    for f in sorted(DATA.glob("*.json")):
        if f.name in ("schema.json", "stats.json"):
            continue
        data = json.loads(f.read_text())
        total += len(data)
        try:
            jsonschema.validate(data, schema)
            print(f"  ✓ {f.name}: {len(data)} items valid")
        except jsonschema.ValidationError as e:
            print(f"  ✗ {f.name}: {e.message}")
            print(f"    Path: {list(e.absolute_path)}")
            errors += 1
    return total, errors


def check_ids():
    all_ids = {}
    dupes = []
    for f in sorted(DATA.glob("*.json")):
        if f.name in ("schema.json", "stats.json"):
            continue
        data = json.loads(f.read_text())
        for item in data:
            rid = item["id"]
            if rid in all_ids:
                dupes.append((rid, all_ids[rid], f.name))
            all_ids[rid] = f.name
    if dupes:
        for rid, f1, f2 in dupes:
            print(f"  ✗ Duplicate ID '{rid}' in {f1} and {f2}")
    else:
        print(f"  ✓ {len(all_ids)} unique IDs, no duplicates")
    return len(dupes)


def check_links_quick():
    missing = 0
    for f in sorted(DATA.glob("*.json")):
        if f.name in ("schema.json", "stats.json"):
            continue
        data = json.loads(f.read_text())
        for item in data:
            has_link = any(item.get(k) for k in ("paper", "repo", "website"))
            if not has_link:
                print(f"  ⚠ {f.name}: '{item['id']}' has no paper/repo/website link")
                missing += 1
    if missing == 0:
        print("  ✓ All items have at least one link")
    return missing


def check_what_length():
    errors = 0
    for f in sorted(DATA.glob("*.json")):
        if f.name in ("schema.json", "stats.json"):
            continue
        data = json.loads(f.read_text())
        for item in data:
            what = item.get("what", "")
            if len(what) > 200:
                print(f"  ✗ {f.name}: '{item['id']}' what is {len(what)} chars (>200): {what[:60]}...")
                errors += 1
    if errors == 0:
        print("  ✓ All what fields are ≤200 characters")
    return errors


def main():
    print("=== Schema Validation ===")
    total, schema_errors = validate_schema()

    print("\n=== What Length Check ===")
    what_errors = check_what_length()

    print("\n=== ID Uniqueness ===")
    id_errors = check_ids()

    print("\n=== Link Presence ===")
    link_warnings = check_links_quick()

    print(f"\n=== Summary ===")
    print(f"Total items: {total}")
    print(f"Schema errors: {schema_errors}")
    print(f"What length errors: {what_errors}")
    print(f"Duplicate IDs: {id_errors}")
    print(f"Missing links: {link_warnings}")

    if schema_errors or id_errors or what_errors:
        sys.exit(1)
    print("\n✓ All checks passed")


if __name__ == "__main__":
    main()
