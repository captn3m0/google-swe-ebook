#!/usr/bin/env python
import sys
import panflute as pf

KNOWN_CHAPTERS = [
    "foreword",
    "preface",
    "what-is-software-engineering",
    "how-to-work-well-on-teams",
    "knowledge-sharing",
    "engineering-for-equity",
    "how-to-lead-a-team",
    "leading-at-scale",
    "measuring-engineering-productivity",
    "style-guides-and-rules",
    "code-review",
    "documentation",
    "testing-overview",
    "unit-testing",
    "test-doubles",
    "larger-testing",
    "deprecation",
    "version-control-and-branch-management",
    "code-search",
    "build-systems-and-build-philosophy",
    "critique-googles-code-review-tool",
    "static-analysis-1",
    "dependency-management",
    "large-scale-changes",
    "continuous-integration",
    "continuous-delivery-1",
    "compute-as-a-service",
    "afterword"
]

def filter_content(elem, doc):
    if isinstance(elem, pf.Header):
        if elem.identifier in KNOWN_CHAPTERS or elem.identifier.startswith('part-'):
            elem.level -= 1

    if isinstance(elem, pf.Link):
        # Change references to use square brackets
        if len(elem.content) == 1:
            if isinstance(elem.content[0], pf.Str):
                elem.content = [pf.Str(f"[{elem.content[0].text}]")]
        # Convert all .html internal links to direct internal links
        if elem.url.split("#")[0].endswith(".html"):
            elem.url = "#" + elem.url.split("#")[-1]
            elem.attributes = {}
        # And the identifiers for footnotes are paragraph attributes
        # which pandoc drops, so we add these attributes back
        # into the links
        if elem.url.endswith("-marker"):
            elem.identifier = elem.url[1:-7]

if __name__ == "__main__":
    pf.toJSONFilter(filter_content)