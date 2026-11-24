#!/usr/bin/env python3
"""Alien Field Notes: The Two Day Earth Review.

Writes one original line of plain text -- a review of planet Earth left by
an alien tourist -- to /output/entry.txt. Stdlib only; no third-party
dependencies, so it runs in a plain python:3.13-slim sandbox.
"""

import os

ENTRY = (
    "The locals built a box that dings when dinner is ready, then ignore it "
    "for twenty minutes to finish one more episode. Earth, 4/5 \u2014 the "
    "snacks justify the light-years."
)


def main() -> None:
    text = ENTRY.strip()
    assert 1 <= len(text) <= 200, f"entry is {len(text)} characters, must be 1-200"
    assert text == text.strip() and text, "entry must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(text)


if __name__ == "__main__":
    main()
