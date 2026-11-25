#!/usr/bin/env python3
"""Midnight Fridge Roast — make.fun entry.

Writes a single one-line roast of a smart fridge that refuses to open
after midnight to /output/entry.txt. Pure standard library, fully
deterministic: the same line every run.
"""

import os

ROAST = "My fridge locks at midnight like the leftovers filed a restraining order against me."

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    line = ROAST.strip()
    assert 1 <= len(line) <= 200, "roast must be 1-200 characters"
    assert "\n" not in line, "roast must be a single line"
    assert line and not line.isspace(), "roast must not be blank"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(line)
    # Read back what we wrote: the judge only ever sees this file.
    with open(OUTPUT_PATH, encoding="utf-8") as f:
        written = f.read()
    assert written == line, "round-trip mismatch"
    print(f"wrote {len(written)} chars to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
