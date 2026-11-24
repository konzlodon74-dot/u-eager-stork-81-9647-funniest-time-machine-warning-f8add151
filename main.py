#!/usr/bin/env python3
"""Funniest Time Machine Warning Label.

Writes one line -- the funniest warning label for a time machine -- to
/output/entry.txt. Stdlib only, deterministic.
"""

import os

# The label, in the flat voice of a real safety notice: it turns the
# classic hazard of meeting your own past self into the joke, and saves
# the sting for the last three words -- your double does not merely know
# what you will say, he already hates it.
LABEL = (
    "WARNING: If you meet yourself, do not speak. "
    "He already knows what you'll say, and he hates it."
)


def main() -> None:
    if not 1 <= len(LABEL) <= 120:
        raise ValueError("label must be 1-120 characters")
    if "\n" in LABEL or LABEL != LABEL.strip():
        raise ValueError("label must be exactly one line")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LABEL + "\n")
    print(LABEL)


if __name__ == "__main__":
    main()
