"""Prepare a bounded issue preview without modifying the full reports."""
import os
from pathlib import Path


def issue_body(report, run_url):
    limit = 60000
    encoded = report.encode("utf-8")
    if len(encoded) <= limit:
        return report
    notice = (
        "\n\nReport preview truncated. Full Markdown and JSON reports: "
        f"{run_url}#artifacts\n"
    )
    preview = encoded[:limit - len(notice.encode("utf-8"))].decode("utf-8", errors="ignore")
    return preview + notice


if __name__ == "__main__":
    run_url = (
        f"{os.environ['GITHUB_SERVER_URL']}/{os.environ['GITHUB_REPOSITORY']}"
        f"/actions/runs/{os.environ['GITHUB_RUN_ID']}"
    )
    report = Path("link-check-report.md").read_bytes().decode("utf-8")
    Path("link-check-issue.md").write_bytes(issue_body(report, run_url).encode("utf-8"))
