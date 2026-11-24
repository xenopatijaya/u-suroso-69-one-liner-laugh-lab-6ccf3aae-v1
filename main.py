#!/usr/bin/env python3
"""One-Liner Laugh Lab entry.

Writes one short funny line to /output/entry.txt: the excuse a robot
vacuum gives after eating a sock. Python standard library only.
"""

import os

ENTRY = (
    "I didn't eat your sock \u2014 I gave it a guided tour "
    "of my dustbin, and it refused to leave."
)


def main():
    # The gate requires 1-200 characters of UTF-8 text, not only whitespace.
    if not 1 <= len(ENTRY) <= 200 or not ENTRY.strip():
        raise SystemExit("entry fails the 1-200 character gate")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(ENTRY)
    print(ENTRY)


if __name__ == "__main__":
    main()
