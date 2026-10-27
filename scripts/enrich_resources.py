"""Assign stable IDs and conservative search facets to catalog records.

The script only fills missing derived metadata. Existing IDs/facets are preserved.
Run with --apply once to persist the migration, then --check in CI.
"""
import argparse
import hashlib
import json
import re
from pathlib import Path
from urllib.parse import urlsplit

ROOT = Path(__file__).resolve().parents[1]
RESOURCES = ROOT / "resources.json"
PROJECT_GROUPS = ROOT / "index" / "project-groups.json"
ID_PATTERN = re.compile(r"[^a-z0-9]+")


def slug(value):
    return ID_PATTERN.sub("-", value.casefold()).strip("-")


def norm_url(value):
    return value.strip().rstrip("/").casefold()


def load_project_groups():
    if not PROJECT_GROUPS.exists():
        return {}
    result = {}
    groups = json.loads(PROJECT_GROUPS.read_text(encoding="utf-8"))
    for group in groups.get("groups", []):
        for url in group["urls"]:
            result[norm_url(url)] = group["project_id"]
    return result


# A small vocabulary of discovery facets; these are not claims about support.
TOPIC_PATTERNS = {
    "accessibility": r"\b(accessibility|a11y|wcag)\b",
    "ai": r"\b(ai|artificial intelligence|machine learning|ml)\b",
    "android": r"\b(android|adb)\b",
    "api-design": r"\b(api design|api contract|openapi|swagger|rest api)\b",
    "api-integration": r"\b(api|sdk|http client|rest client|grpc|graphql)\b",
    "architecture": r"\b(architecture|system design|microservices|design pattern)\b",
    "browser-automation": r"\b(browser automation|playwright|webdriver|selenium|puppeteer)\b",
    "build-tools": r"\b(build system|compiler|bundler|package manager|build tool)\b",
    "cloud": r"\b(cloud|aws|azure|google cloud|serverless)\b",
    "containers": r"\b(container|docker|podman|kubernetes|k8s)\b",
    "data-science": r"\b(data science|data analysis|data engineering|dataset|analytics)\b",
    "database": r"\b(database|postgres|postgresql|mysql|sqlite|redis|sql|orm)\b",
    "design-systems": r"\b(design system|design token|component library|ui kit)\b",
    "desktop": r"\b(desktop|electron|tauri|winui|wpf|qt)\b",
    "end-to-end-testing": r"\b(end.to.end|e2e|integration test|browser test)\b",
    "elixir": r"\belixir\b",
    "game-development": r"\b(game|gaming|game engine)\b",
    "git": r"\b(git|version control|repository)\b",
    "go": r"\b(golang|go language)\b",
    "haskell": r"\bhaskell\b",
    "infrastructure-as-code": r"\b(terraform|infrastructure as code|iac|pulumi|ansible)\b",
    "java": r"\bjava\b",
    "javascript": r"\b(javascript|node\.js|nodejs)\b",
    "kotlin": r"\bkotlin\b",
    "linux": r"\blinux\b",
    "llm": r"\b(llm|large language model|language model)\b",
    "mobile": r"\b(mobile|ios|android|flutter|react native)\b",
    "mcp": r"\b(model context protocol|mcp server|mcp)\b",
    "observability": r"\b(observability|monitoring|metrics|tracing|logging|profiling)\b",
    "php": r"\bphp\b",
    "python": r"\bpython\b",
    "ruby": r"\bruby\b",
    "rust": r"\brust\b",
    "security": r"\b(security|vulnerability|vulnerabilities|secure|supply.chain|threat)\b",
    "swift": r"\bswift\b",
    "testing": r"\b(test|testing|test automation|benchmark|fuzzing|quality assurance)\b",
    "typescript": r"\btypescript\b",
    "web": r"\b(web application|web framework|frontend|front.end|website|web interface)\b",
    "windows": r"\b(windows|win32|winui|winrt|msvc)\b",
}
LANGUAGES = {"elixir", "go", "haskell", "java", "javascript", "kotlin", "php", "python", "ruby", "rust", "swift", "typescript"}


def resource_type(row):
    name = row["name"].casefold()
    purpose = row["purpose"].casefold()
    url = urlsplit(row["url"])
    host = url.netloc.casefold().removeprefix("www.")
    path = url.path.casefold()
    category = row["category"].casefold()
    text = name + " " + purpose

    if category == "ui design inspiration and reference":
        return "design-reference"
    if any(token in text for token in ("awesome list", "curated list", "collection of links", "collection of resources")) or name.startswith("awesome-"):
        return "curated-list"
    if any(token in text for token in ("dataset", "datasets", "data set")):
        return "dataset"
    if any(token in text for token in ("course", "curriculum", "tutorial series", "learning path")):
        return "course"
    if host == "github.com" or host.endswith(".github.io") or host == "codeberg.org":
        return "repository"
    if host.startswith(("doc.", "docs.", "developer.", "developers.", "learn.")) or host == "go.dev" or any(part in path.split("/") for part in ("doc", "docs", "documentation", "learn", "reference")):
        return "documentation"
    if any(token in category for token in ("documentation", "learning and references")):
        return "documentation"
    if any(token in category for token in ("service", "providers", "business sdk")):
        return "service"
    if any(token in category for token in ("design systems", "design inspiration")):
        return "design-reference"
    standard_evidence = re.search(r"\b(standard specification|technical standard|interface standard|file[- ]format standard|web platform standards?|specification|rfc(?:\s?\d+)?)\b", text, re.I)
    if standard_evidence or ("standards" in category and re.search(r"\b(standard|specification|rfc|w3c|ietf)\b", text, re.I)):
        return "standard"
    return "reference"


def topic_facets(row):
    text = " ".join((row["name"], row["purpose"], row["category"])).casefold()
    topics = {topic for topic, pattern in TOPIC_PATTERNS.items() if re.search(pattern, text, re.I)}
    # The standalone language name is meaningful only in a language-focused category.
    if row["name"].strip().casefold() == "go" and "language" in row["category"].casefold():
        topics.add("go")
    return sorted(topics)


def use_cases(row):
    category = row["category"].casefold()
    mappings = (
        (("test", "verification", "performance"), "test-and-verify-software"),
        (("security", "identity"), "assess-and-secure-systems"),
        (("design", "web interfaces"), "research-or-build-interfaces"),
        (("cloud", "infrastructure", "backup", "observability", "ci version", "builds"), "deploy-and-operate-software"),
        (("database", "data science", "public data", "search messaging"), "store-query-or-process-data"),
        (("api contracts", "integration apis"), "design-or-integrate-apis"),
        (("ai ", "ai mcp", "ai models", "ai retrieval"), "build-or-evaluate-ai-systems"),
        (("language", "python rust", ".net", "platform sdks", "niche language"), "implement-with-a-language-or-sdk"),
        (("android", "desktop mobile", "windows", "world of warcraft"), "build-or-debug-platform-software"),
        (("accessibility", "documents"), "document-or-improve-accessibility"),
        (("game creation", "graphics multimedia"), "build-games-or-media-software"),
    )
    values = [value for fragments, value in mappings if any(fragment in category for fragment in fragments)]
    return sorted(set(values or ["develop-or-learn-software"]))


def audiences(row):
    category = row["category"].casefold()
    values = set()
    if any(x in category for x in ("test", "verification", "performance")):
        values.update(("software-developer", "test-engineer"))
    if "security" in category:
        values.update(("software-developer", "security-engineer"))
    if any(x in category for x in ("design", "web interfaces")):
        values.update(("frontend-developer", "designer"))
    if any(x in category for x in ("cloud", "infrastructure", "observability", "backup")):
        values.update(("platform-engineer", "operations-engineer"))
    if category.startswith("ai "):
        values.update(("software-developer", "ai-engineer"))
    if any(x in category for x in ("language", "python rust", ".net", "platform sdk", "niche language")):
        values.add("software-developer")
    return sorted(values or {"software-developer"})


def verification_level(row):
    review = row["review"].casefold()
    status = str(row.get("http_status", "")).casefold()
    if row["source"] == "user-requested" or "user-provided url" in review:
        return "user-submitted"
    if any(marker in review + " " + status for marker in ("github repository metadata checked", "github api", "repository api")):
        return "repository-metadata"
    if "readme" in review and ("license" in review or "metadata" in review):
        return "source-excerpt-reviewed"
    if any(marker in review for marker in ("selected pages fetched", "http 200", "source inspection", "source checked")) or "documentation fetched" in status:
        return "page-fetch-or-source-check"
    if "historical discovery" in review:
        return "historical-notes"
    if re.fullmatch(r"\s*\d{3}\s*", status):
        return "historical-link-check"
    return "not-recorded"


def github_project_id(url):
    parsed = urlsplit(url)
    parts = [part for part in parsed.path.strip("/").split("/") if part]
    if parsed.netloc.casefold() not in ("github.com", "www.github.com") or len(parts) < 2:
        return None
    reserved = {"topics", "collections", "sponsors", "orgs", "login", "features", "marketplace", "settings", "search", "about", "apps", "enterprise", "site", "notifications"}
    if parts[0].casefold() in reserved:
        return None
    owner, repository = parts[:2]
    return f"github:{owner.casefold()}/{repository.casefold()}"


def enrich(rows):
    manual_groups = load_project_groups()
    seen_ids = set()
    for row in rows:
        category_id = slug(row["category"])
        row.setdefault("category_id", category_id)
        if not row.get("resource_id"):
            identity = "\n".join((row["source"], category_id, norm_url(row["url"]), row["name"].casefold()))
            digest = hashlib.sha256(identity.encode("utf-8")).hexdigest()[:12]
            row["resource_id"] = f"res-{slug(row['name'])[:42]}-{digest}"
        if row["resource_id"] in seen_ids:
            raise ValueError(f"Duplicate resource_id: {row['resource_id']}")
        seen_ids.add(row["resource_id"])

        row.setdefault("resource_type", resource_type(row))
        row.setdefault("topics", topic_facets(row))
        row.setdefault("use_cases", use_cases(row))
        row.setdefault("languages", sorted(set(row["topics"]) & LANGUAGES))
        row.setdefault("platforms", sorted(set(row["topics"]) & {"android", "linux", "windows", "mobile", "web"}))
        row.setdefault("audiences", audiences(row))
        row.setdefault("related_resource_ids", [])

        manual_id = manual_groups.get(norm_url(row["url"]))
        repo_id = github_project_id(row["url"])
        if manual_id:
            row.setdefault("project_id", manual_id)
        elif repo_id:
            row.setdefault("project_id", repo_id)
        if not row.get("verification_level"):
            row["verification_level"] = verification_level(row)
        match = re.search(r"surfaced via ([^;]+)", row["review"], re.I)
        if match:
            row.setdefault("discovery_source", match.group(1).strip())

    grouped = {}
    for row in rows:
        project_id = row.get("project_id")
        if project_id:
            grouped.setdefault(project_id, []).append(row["resource_id"])
    relationships = {row["resource_id"]: set(row.get("related_resource_ids", [])) for row in rows}
    for row in rows:
        project_id = row.get("project_id")
        siblings = grouped.get(project_id, []) if project_id else []
        relationships[row["resource_id"]].update(i for i in siblings if i != row["resource_id"])
    for resource_id, related_ids in relationships.items():
        unknown = related_ids - relationships.keys()
        if unknown:
            raise ValueError(f"Unknown related resource IDs for {resource_id}: {sorted(unknown)}")
        for related_id in related_ids:
            relationships[related_id].add(resource_id)
    for row in rows:
        row["related_resource_ids"] = sorted(relationships[row["resource_id"]])
    return rows


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--apply", action="store_true", help="write missing IDs and facets to resources.json")
    mode.add_argument("--check", action="store_true", help="fail if any required derived field is missing")
    mode.add_argument("--refresh-types", action="store_true", help="recalculate only the derived resource_type facet using current rules")
    mode.add_argument("--refresh-topics", action="store_true", help="recalculate topic and language facets using current rules")
    mode.add_argument("--refresh-verification", action="store_true", help="recalculate only the derived verification_level facet")
    args = parser.parse_args()
    original = json.loads(RESOURCES.read_text(encoding="utf-8"))
    if args.refresh_verification:
        refreshed = 0
        for row in original:
            value = verification_level(row)
            if row.get("verification_level") != value:
                row["verification_level"] = value
                refreshed += 1
        RESOURCES.write_text(json.dumps(original, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        print(f"Refreshed verification_level on {refreshed} records; all other catalog fields were preserved.")
        return
    if args.refresh_topics:
        refreshed = 0
        for row in original:
            topics = topic_facets(row)
            languages = sorted(set(topics) & LANGUAGES)
            if row.get("topics") != topics or row.get("languages") != languages:
                row["topics"] = topics
                row["languages"] = languages
                refreshed += 1
        RESOURCES.write_text(json.dumps(original, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        print(f"Refreshed topic and language facets on {refreshed} records; all other catalog fields were preserved.")
        return
    if args.refresh_types:
        refreshed = 0
        for row in original:
            value = resource_type(row)
            if row.get("resource_type") != value:
                row["resource_type"] = value
                refreshed += 1
        RESOURCES.write_text(json.dumps(original, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        print(f"Refreshed resource_type on {refreshed} records; all other catalog fields were preserved.")
        return
    enriched = enrich(json.loads(json.dumps(original)))
    required = ("resource_id", "category_id", "resource_type", "topics", "use_cases", "languages", "platforms", "audiences", "related_resource_ids", "verification_level")
    missing = [(r.get("name"), key) for r in enriched for key in required if key not in r]
    if missing:
        raise SystemExit(f"Missing enriched metadata: {missing[:10]}")
    if args.apply:
        RESOURCES.write_text(json.dumps(enriched, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        print(f"Enriched {len(enriched)} records in resources.json; existing records and IDs were preserved.")
    else:
        if any(any(k not in r for k in required) for r in original):
            raise SystemExit("Catalog needs enrichment; run scripts/enrich_resources.py --apply")
        if [r["resource_id"] for r in enriched] != [r["resource_id"] for r in original]:
            raise SystemExit("Stable resource IDs would change; inspect before applying.")
        print(f"Checked enriched metadata for {len(original)} records.")


if __name__ == "__main__":
    main()
