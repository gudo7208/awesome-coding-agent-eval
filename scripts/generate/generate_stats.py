#!/usr/bin/env python3
"""Generate data/stats.json from data/*.json."""
import json
from collections import Counter
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DATA = ROOT / "data"
OUT = DATA / "stats.json"


def load_all():
    items = []
    by_stage = {}
    for f in DATA.glob("*.json"):
        if f.name in ("schema.json", "stats.json"):
            continue
        data = json.loads(f.read_text())
        items.extend(data)
        by_stage[f.stem] = len(data)
    return items, by_stage


def generate():
    items, by_stage = load_all()
    total = len(items)

    by_subcategory = Counter(i.get("subcategory", "unknown") for i in items)
    by_type = Counter(i.get("type", "unknown") for i in items)
    by_status = Counter(i.get("status", "active") for i in items)

    all_langs = []
    for i in items:
        all_langs.extend(i.get("languages", []))
    by_language = Counter(all_langs)

    all_methods = [i.get("eval_method") for i in items if i.get("eval_method")]
    by_eval_method = Counter(all_methods)

    all_tags = []
    for i in items:
        all_tags.extend(i.get("tags", []))
    top_tags = Counter(all_tags).most_common(20)

    stats = {
        "total": total,
        "by_stage": dict(sorted(by_stage.items())),
        "by_subcategory": dict(by_subcategory.most_common()),
        "by_type": dict(by_type.most_common()),
        "by_status": dict(by_status.most_common()),
        "by_language": dict(by_language.most_common()),
        "by_eval_method": dict(by_eval_method.most_common()),
        "top_tags": [{"tag": t, "count": c} for t, c in top_tags],
        "last_updated": date.today().isoformat(),
    }

    OUT.write_text(json.dumps(stats, indent=2, ensure_ascii=False) + "\n")
    print(f"Generated {OUT} (total: {total})")


if __name__ == "__main__":
    generate()
