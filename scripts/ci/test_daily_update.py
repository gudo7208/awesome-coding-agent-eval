#!/usr/bin/env python3
"""Behavior tests for the unattended daily collection pipeline."""

import unittest

from daily_update import deduplicate


class DailyUpdateDeduplicationTest(unittest.TestCase):
    def test_versioned_arxiv_candidate_matches_unversioned_corpus_url(self):
        candidates = [
            {
                "title": "ICAE-Bench",
                "link": "https://arxiv.org/abs/2607.21217v1",
            }
        ]
        existing_urls = {"https://arxiv.org/abs/2607.21217"}

        self.assertEqual([], deduplicate(candidates, existing_urls))


if __name__ == "__main__":
    unittest.main()
