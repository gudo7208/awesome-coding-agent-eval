"""Single source of truth for the controlled vocabulary.

Imported by audit.py, merge_classified.py, and merge_duplicates.py.
classify_candidates.py embeds the same lists inside its LLM prompt string
(it cannot import a Python set into a prompt) — keep that copy in sync by hand.
"""

# subcategory must come from the set for its stage
VALID_SUBCATEGORIES = {
    "benchmark": {
        "bug-fix", "end-to-end", "long-horizon", "large-codebase",
        "code-review", "testing", "security", "production", "code-generation",
        "multi-agent", "feature-development",
    },
    "methodology": {"llm-judge", "process-eval", "execution-based", "hybrid", "human-eval"},
    "toolchain": {"harness", "sandbox", "observability", "judge-tool"},
    "leaderboard": {"se-agent", "code-generation", "activity"},
    "meta-analysis": {"limitation", "quality-study", "blog", "survey"},
}

VALID_EVAL_METHODS = {"execution-based", "llm-judge", "hybrid", "human-eval"}

# cross-reference buckets inside an entry's `related` object.
# Note: the data uses by-stage buckets (benchmarks/toolchain/methodology) in
# addition to the four originally-schema'd ones — all are cleaned/redirected.
RELATED_KEYS = (
    "harness", "leaderboard", "meta_analysis", "variants",
    "benchmarks", "toolchain", "methodology",
)
