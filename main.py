#!/usr/bin/env python3
"""A house cat files a one-star complaint about its human.

Drops one short single-line review into /output/entry.txt.
Same fixed wording on every run: no randomness, no network, no input.
"""

from pathlib import Path

RATING = "\u2605" + "\u2606" * 4
COMPLAINT = (
    "He moved me off his laptop mid-sentence "
    "\u2014 my novel was nearly finished. One star. "
    "The warm spot is still mine. I have already forgiven him. Once."
)
REVIEW = RATING + " " + COMPLAINT

DEST = Path("/output/entry.txt")


def check_line(line: str) -> str:
    """Trim and enforce the competition's single-line length gate."""
    cleaned = line.strip()
    if not 1 <= len(cleaned) <= 200:
        raise ValueError(f"line must be 1-200 chars, got {len(cleaned)}")
    if any(mark in cleaned for mark in ("\n", "\r")):
        raise ValueError("line must fit on a single line")
    if not cleaned.startswith("\u2605"):
        raise ValueError("line must open with the star rating")
    return cleaned


def main() -> None:
    line = check_line(REVIEW)
    DEST.parent.mkdir(parents=True, exist_ok=True)
    DEST.write_text(line, encoding="utf-8")


if __name__ == "__main__":
    main()
