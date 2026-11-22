"""Compare website papers with the CV bibliography.

Run: uv run --with pyyaml scripts/check_publications.py
Invited talks and the thesis are maintained separately.
"""

from pathlib import Path
import re
import unicodedata

import yaml


ROOT = Path(__file__).resolve().parents[1]


def normalize(title):
    title = unicodedata.normalize("NFKD", title).casefold()
    return re.sub(r"[^a-z0-9]", "", title)


def bib_field(entry, name):
    matches = list(re.finditer(r"\b" + name + r"\s*=\s*\{", entry, re.I))
    if not matches:
        return ""
    start = matches[-1].end()
    depth = 1
    for index in range(start, len(entry)):
        if entry[index] == "{" and entry[index - 1] != "\\":
            depth += 1
        elif entry[index] == "}" and entry[index - 1] != "\\":
            depth -= 1
            if depth == 0:
                return entry[start:index]
    raise ValueError(f"Unclosed bibliography field: {name}")


def main():
    records = yaml.safe_load((ROOT / "_data/publications.yml").read_text(encoding="utf-8"))
    website = {
        normalize(record["title"]): record["title"]
        for record in records
        if record["type"] in {"journal", "conference", "preprint"}
    }
    source = (ROOT / "cv-src/publications.bib").read_text(encoding="utf-8")
    source = "\n".join(line for line in source.splitlines() if not line.lstrip().startswith("%"))
    cv = {}
    for entry in re.split(r"(?m)^[ \t]*@", source)[1:]:
        keywords = {word.strip() for word in bib_field(entry, "keywords").split(",")}
        if keywords & {"peerjournal", "peerconf", "preprint"}:
            title = bib_field(entry, "title")
            cv[normalize(title)] = title
    for label, missing in (("Missing from website", cv.keys() - website.keys()),
                           ("Missing from CV", website.keys() - cv.keys())):
        for key in sorted(missing):
            print(f"{label}: {cv.get(key, website.get(key))}")
    if cv.keys() != website.keys():
        raise SystemExit(1)
    print(f"Website and CV agree on {len(cv)} paper titles.")


if __name__ == "__main__":
    main()
