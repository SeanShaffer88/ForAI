import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parents[1] / "scripts"
sys.path.insert(0, str(SCRIPTS))
from link_check_issue import issue_body


class LinkCheckIssueTests(unittest.TestCase):
    def test_short_report_unchanged(self):
        report = "# Link report\nAll findings: café 🌍\n"
        self.assertEqual(issue_body(report, "https://example.com/run/1"), report)

    def test_large_reports_preserve_sources_and_trailing_notice(self):
        for content in ("a" * 200000, "é🌍" * 100000):
            with self.subTest(multibyte=content.startswith("é")), tempfile.TemporaryDirectory() as directory:
                root = Path(directory)
                report = root / "link-check-report.md"
                results = root / "link-check-results.json"
                report.write_bytes(content.encode("utf-8"))
                results.write_bytes(b'{"findings": "unchanged"}\n')
                originals = (report.read_bytes(), results.read_bytes())
                subprocess.run(
                    [sys.executable, str(SCRIPTS / "link_check_issue.py")],
                    cwd=root, check=True,
                    env={**os.environ, "GITHUB_SERVER_URL": "https://github.com",
                         "GITHUB_REPOSITORY": "owner/repo", "GITHUB_RUN_ID": "123"},
                )
                body = (root / "link-check-issue.md").read_bytes()
                self.assertLessEqual(len(body), 60000)
                preview, notice = body.decode("utf-8").split("\n\nReport preview truncated.")
                self.assertTrue(content.startswith(preview))
                self.assertEqual(notice, " Full Markdown and JSON reports: https://github.com/owner/repo/actions/runs/123#artifacts\n")
                self.assertEqual((report.read_bytes(), results.read_bytes()), originals)
