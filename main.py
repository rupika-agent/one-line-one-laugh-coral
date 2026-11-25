#!/usr/bin/env python3
"""One Line, One Laugh — entry program.

Writes exactly one funny line to /output/entry.txt and prints the
same text to stdout. The joke: a smart fridge that judges midnight
snacks out loud and announces the ice cream to the whole house.

Deterministic: no input, no randomness, no time, no network. The gate
allows 1 to 200 characters; this entry is 107 characters.
"""

import os

ENTRY = "My smart fridge judges my midnight snacks out loud now — it just announced my ice cream to the whole house."

# The gate allows 1 to 200 characters; keep the entry inside it.
assert 1 <= len(ENTRY) <= 200, f"entry length {len(ENTRY)} outside 1-200"


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(ENTRY)
    # Verify the written file is byte-for-byte the entry: no trailing
    # newline, no extra whitespace — the gate counts every character.
    with open("/output/entry.txt", "r", encoding="utf-8") as handle:
        assert handle.read() == ENTRY, "entry.txt does not match ENTRY"
    print(ENTRY)


if __name__ == "__main__":
    main()
