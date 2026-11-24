#!/usr/bin/env python3
"""Alien Field Notes: The Two Day Earth Review.

Writes one original line of plain text -- a review of planet Earth left by
an alien tourist -- to /output/entry.txt. Stdlib only; no third-party
dependencies, so it runs in a plain python:3.13-slim sandbox.
"""

import os
import sys

# One line, at most 200 characters: the alien tourist's review of Earth.
# The joke is one concrete observation (the dinner-ready ding, ignored for
# one more episode), with the verdict and the punch at the end.
ENTRY = (
    "The locals built a box that dings when dinner is ready, then ignore it "
    "for twenty minutes to finish one more episode. Earth, 4/5 \u2014 the "
    "snacks justify the light-years."
)

MAX_CHARS = 200


def validate_entry(text: str) -> str:
    """Return the entry stripped, or fail loudly if it breaks the gate."""
    entry = text.strip()
    if not entry:
        raise ValueError("entry must not be empty or only whitespace")
    if len(entry) > MAX_CHARS:
        raise ValueError(
            f"entry is {len(entry)} characters, over the {MAX_CHARS} limit"
        )
    if "\n" in entry or "\r" in entry:
        raise ValueError("entry must be a single line")
    return entry


def write_entry(text: str, path: str = "/output/entry.txt") -> None:
    """Write the validated entry as UTF-8 text with no trailing newline."""
    entry = validate_entry(text)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(entry)


def main() -> int:
    try:
        write_entry(ENTRY)
    except ValueError as exc:
        print(f"invalid entry: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
