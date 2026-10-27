import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from search import rank_results


class SearchTests(unittest.TestCase):
    def setUp(self):
        self.rows = [
            {
                "resource_id": "res-secure-build-1",
                "name": "Secure Build Toolkit",
                "purpose": "Find supply-chain vulnerabilities in software builds.",
                "category": "Security testing",
                "topics": ["security", "testing"],
                "use_cases": ["assess-and-secure-systems"],
                "resource_type": "repository",
                "languages": ["python"],
                "platforms": ["linux"],
                "audiences": ["security-engineer"],
                "review": "Compatibility audit required; historical security audit notes.",
                "http_status": "404",
                "source": "legacy-security-audit",
            },
            {
                "resource_id": "res-web-test-2",
                "name": "Browser Test Runner",
                "purpose": "Automate end-to-end tests for web applications.",
                "category": "Testing",
                "topics": ["testing", "web", "browser-automation"],
                "use_cases": ["test-and-verify-software"],
                "resource_type": "repository",
                "languages": ["javascript"],
                "platforms": ["web"],
                "audiences": ["test-engineer"],
                "review": "Security audit, compatibility audit, and software audit were recorded.",
                "http_status": "200",
                "source": "legacy",
            },
        ]

    def test_boilerplate_is_not_searchable(self):
        self.assertEqual(rank_results(self.rows, "compatibility audit"), [])

    def test_all_terms_must_match_and_name_is_weighted(self):
        results = rank_results(self.rows, "build security")
        self.assertEqual([row["resource_id"] for _, row in results], ["res-secure-build-1"])
        name_first = rank_results(self.rows, "browser tests")
        self.assertEqual(name_first[0][1]["resource_id"], "res-web-test-2")

    def test_facets_are_exact_and_composable(self):
        results = rank_results(self.rows, "test", topic="browser-automation", language="javascript", platform="web")
        self.assertEqual([row["resource_id"] for _, row in results], ["res-web-test-2"])
        self.assertEqual(rank_results(self.rows, "test", language="python", platform="web"), [])

    def test_short_terms_do_not_match_inside_unrelated_words(self):
        self.rows[0]["purpose"] = "We maintain build pipelines."
        self.assertEqual(rank_results(self.rows, "ai"), [])

    def test_blank_query_is_safe(self):
        self.assertEqual(rank_results(self.rows, "   "), [])


if __name__ == "__main__":
    unittest.main()
