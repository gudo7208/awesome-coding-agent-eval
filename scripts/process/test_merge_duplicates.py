#!/usr/bin/env python3
"""Regression tests for merge_duplicates.py — the data-loss edge cases.

Runs against a temporary data dir (never touches data/). Both pytest-discoverable
(test_* functions) and runnable directly: `.venv/bin/python scripts/process/test_merge_duplicates.py`.
"""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import merge_duplicates as M  # noqa: E402


def _run(tmp_path, entries, ops):
    """Write entries + ops into tmp_path, run main() with --apply, return id->entry."""
    data_dir = tmp_path / "data"
    data_dir.mkdir(parents=True, exist_ok=True)
    (data_dir / "benchmarks.json").write_text(json.dumps(entries, ensure_ascii=False, indent=2) + "\n")
    ops_file = tmp_path / "ops.json"
    ops_file.write_text(json.dumps(ops))
    M.DATA = data_dir
    sys.argv = ["merge_duplicates.py", "--ops", str(ops_file), "--apply"]
    M.main()
    result = json.loads((data_dir / "benchmarks.json").read_text())
    return {e["id"]: e for e in result}


def _e(eid, **kw):
    base = {"id": eid, "name": eid, "stage": "benchmark", "subcategory": "end-to-end",
            "what": eid, "type": "paper", "tags": ["t"], "paper": f"http://x/{eid}"}
    base.update(kw)
    return base


def test_chain_redirect_lands_on_terminal(tmp_path):
    # A->B->C : a reference to A must end up on C, and both A and B are deleted.
    entries = [_e("a"), _e("b"), _e("c"),
               _e("ref", related={"variants": ["a", "b"]})]
    out = _run(tmp_path, entries, {"merge": {"a": "b", "b": "c"}})
    assert set(out) == {"c", "ref"}, "A and B must be removed, C kept"
    assert out["ref"]["related"]["variants"] == ["c"], "refs to A and B collapse onto C"


def test_missing_canonical_does_not_delete_dup(tmp_path):
    # canonical doesn't exist -> the dup must survive (no silent data loss).
    entries = [_e("x"), _e("keep")]
    out = _run(tmp_path, entries, {"merge": {"x": "nonexistent"}})
    assert "x" in out, "dup must NOT be deleted when its canonical is missing"


def test_self_merge_is_skipped(tmp_path):
    # A->A must not destroy A nor double its related list.
    entries = [_e("y", related={"variants": ["keep"]}), _e("keep")]
    out = _run(tmp_path, entries, {"merge": {"y": "y"}})
    assert "y" in out, "self-merge must not delete the entry"
    assert out["y"]["related"]["variants"] == ["keep"], "self-merge must not duplicate refs"


def test_set_fields_cannot_change_id(tmp_path):
    entries = [_e("z"), _e("ref", related={"variants": ["z"]})]
    out = _run(tmp_path, entries, {"set_fields": {"z": {"id": "zz", "subcategory": "bug-fix"}}})
    assert "z" in out and "zz" not in out, "id must be immutable"
    assert out["z"]["subcategory"] == "bug-fix", "other fields still applied"
    assert out["ref"]["related"]["variants"] == ["z"], "reference stays valid"


def test_fill_missing_preserves_falsy_canonical(tmp_path):
    # canonical has stars=0 (valid) -> must NOT be overwritten by dup's stars.
    entries = [_e("canon", stars=0), _e("dup", stars=99)]
    out = _run(tmp_path, entries, {"merge": {"dup": "canon"}})
    assert out["canon"]["stars"] == 0, "falsy-but-present field must be preserved"


def test_normal_merge_redirects_and_adopts_what(tmp_path):
    # title-dump canonical adopts the dup's better `what`; refs redirect.
    entries = [_e("canon", what="canon", name="canon"),
               _e("dup", what="A real description", name="dup"),
               _e("ref", related={"variants": ["dup"]})]
    out = _run(tmp_path, entries, {"merge": {"dup": "canon"}})
    assert "dup" not in out
    assert out["canon"]["what"] == "A real description", "adopt non-title-dump what"
    assert out["ref"]["related"]["variants"] == ["canon"], "ref redirected"


if __name__ == "__main__":
    import tempfile
    import traceback
    tests = [v for k, v in sorted(globals().items()) if k.startswith("test_")]
    passed = 0
    for t in tests:
        with tempfile.TemporaryDirectory() as d:
            try:
                t(Path(d))
                print(f"  ✓ {t.__name__}")
                passed += 1
            except Exception:
                print(f"  ✗ {t.__name__}")
                traceback.print_exc()
    print(f"\n{passed}/{len(tests)} passed")
    sys.exit(0 if passed == len(tests) else 1)
