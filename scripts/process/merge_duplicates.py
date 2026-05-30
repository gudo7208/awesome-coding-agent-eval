#!/usr/bin/env python3
"""Merge duplicate entries, redirect references, and patch fields — safely.

Driven by an operations JSON (--ops file.json):

    {
      "merge":       {"<dup_id>": "<canonical_id>", ...},
      "rename_refs": {"<old_ref>": "<new_ref>", ...},
      "set_fields":  {"<id>": {"subcategory": "...", "paper": "..."}, ...}
    }

Semantics
  merge        delete <dup_id>; canonical inherits the union of its `related`
               lists, any scalar fields it was missing, and the dup's `what`
               if the canonical's `what` was just the title verbatim. Every
               reference to <dup_id> across the corpus is redirected to
               <canonical_id>. Merge graphs are resolved transitively, so
               A->B->C lands references and fields on C; self-merges (A->A) and
               merges whose canonical does not exist are skipped (never delete a
               dup whose target is missing).
  rename_refs  replace every reference <old_ref> -> <new_ref> (no entry
               deleted; use when a referenced id was mistyped). Resolved
               transitively together with merges.
  set_fields   overwrite the given fields on <id> in place. The `id` field
               itself cannot be changed (it would orphan every reference).

After every op the tool cleans all `related` lists: dedup, drop self-refs,
drop references to ids that no longer exist.

Dry-run by default; pass --apply to write (atomically).
"""
import argparse
import json
import os
from pathlib import Path

from taxonomy import RELATED_KEYS

ROOT = Path(__file__).resolve().parents[2]
DATA = ROOT / "data"
SKIP = {"schema.json", "stats.json"}
EMPTY = (None, "", [], {})
# scalar fields a canonical may inherit from a duplicate if it lacks them
FILLABLE = ("paper", "repo", "website", "venue", "scale", "stars",
            "eval_method", "granularity", "languages")
TAG_CAP = 5  # matches merge_classified.py


def load():
    files = {}
    for f in sorted(DATA.glob("*.json")):
        if f.name in SKIP:
            continue
        files[f.name] = json.loads(f.read_text())
    return files


def index(files):
    idx = {}
    for fname, entries in files.items():
        for e in entries:
            idx[e["id"]] = (e, fname)
    return idx


def is_title_dump(e):
    w = (e.get("what") or "").strip().rstrip(".").lower()
    n = (e.get("name") or "").strip().rstrip(".").lower()
    return bool(w) and w == n


def resolve(start, raw, all_ids):
    """Follow a redirect chain to its terminal id; None if cyclic or terminal missing."""
    seen = set()
    cur = start
    while cur in raw:
        if cur in seen:        # cycle
            return None
        seen.add(cur)
        cur = raw[cur]
    return cur if cur in all_ids else None


def save_atomic(path: Path, entries):
    tmp = path.with_suffix(".tmp")
    tmp.write_text(json.dumps(entries, ensure_ascii=False, indent=2) + "\n")
    tmp.replace(path)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--ops", required=True)
    ap.add_argument("--apply", action="store_true")
    args = ap.parse_args()

    ops = json.loads(Path(args.ops).read_text())
    merge = ops.get("merge", {})
    rename = ops.get("rename_refs", {})
    set_fields = ops.get("set_fields", {})

    files = load()
    idx = index(files)
    all_ids = set(idx)
    log = []

    # ---- resolve each merge dup to its terminal canonical ----
    # terminal is never a merge key, so it survives deletion.
    final = {}          # dup_id -> terminal canonical id
    for dup_id in merge:
        if dup_id not in idx:
            log.append(f"  [skip] merge dup '{dup_id}' not found")
            continue
        if merge[dup_id] == dup_id:
            log.append(f"  [skip] self-merge '{dup_id}'")
            continue
        target = resolve(dup_id, merge, all_ids)
        if target is None or target == dup_id:
            log.append(f"  [skip] merge '{dup_id}': canonical missing or cyclic")
            continue
        final[dup_id] = target

    # ---- fold each dup into its terminal canonical ----
    for dup_id in sorted(final):          # sorted → deterministic field-fill order
        dup, _ = idx[dup_id]
        canon, _ = idx[final[dup_id]]
        cr = canon.setdefault("related", {})
        for k in RELATED_KEYS:
            merged = list(cr.get(k, []) or []) + list((dup.get("related") or {}).get(k, []) or [])
            if merged:
                cr[k] = merged
        for f in FILLABLE:
            if dup.get(f) not in EMPTY and canon.get(f) in EMPTY:
                canon[f] = dup[f]
        if is_title_dump(canon) and not is_title_dump(dup) and dup.get("what"):
            log.append(f"  [what] '{canon['id']}' adopt what from '{dup_id}'")
            canon["what"] = dup["what"]
        tags = list(canon.get("tags", []))
        for t in dup.get("tags", []):
            if t not in tags:
                tags.append(t)
        canon["tags"] = tags[:TAG_CAP]
        log.append(f"  [merge] '{dup_id}' -> '{final[dup_id]}'")

    # ---- remove only the dups that actually merged ----
    dup_ids = set(final)
    for fname in files:
        files[fname] = [e for e in files[fname] if e["id"] not in dup_ids]

    # ---- redirect map: merges + renames, resolved transitively ----
    raw = dict(rename)
    raw.update(final)
    redirect = {}
    for ref in raw:
        tgt = resolve(ref, raw, all_ids)
        if tgt is not None and tgt != ref:
            redirect[ref] = tgt

    # ---- set_fields (id is immutable) ----
    idx = index(files)
    for eid, fields in set_fields.items():
        if eid not in idx:
            log.append(f"  [skip] set_fields id '{eid}' not found")
            continue
        if "id" in fields:
            log.append(f"  [skip] set_fields '{eid}': refusing to change 'id'")
            fields = {k: v for k, v in fields.items() if k != "id"}
        e, _ = idx[eid]
        for k, v in fields.items():
            e[k] = v
        if fields:
            log.append(f"  [set] '{eid}': {fields}")

    # ---- apply redirects + clean all related lists ----
    valid_ids = set(idx)
    n_redirect = n_drop = 0
    for entries in files.values():
        for e in entries:
            rel = e.get("related")
            if not rel:
                continue
            for k in RELATED_KEYS:
                if k not in rel:
                    continue
                out, seen = [], set()
                for ref in rel[k]:
                    ref2 = redirect.get(ref, ref)
                    if ref2 != ref:
                        n_redirect += 1
                    if ref2 == e["id"] or ref2 not in valid_ids:   # self / dangling
                        n_drop += 1
                        continue
                    if ref2 in seen:                                # dup within list
                        continue
                    seen.add(ref2)
                    out.append(ref2)
                if out:
                    rel[k] = out
                else:
                    rel.pop(k, None)
            if not rel:
                e.pop("related", None)

    # ---- report ----
    for line in log:
        print(line)
    total = sum(len(v) for v in files.values())
    print(f"\n  references redirected: {n_redirect}")
    print(f"  references dropped (self/dangling): {n_drop}")
    print(f"  entries removed (merged): {len(dup_ids)}")
    print(f"  total entries now: {total}")

    if args.apply:
        for fname, entries in files.items():
            save_atomic(DATA / fname, entries)
        print("\n✓ written")
    else:
        print("\n(dry-run — pass --apply to write)")


if __name__ == "__main__":
    main()
