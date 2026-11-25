"""Writes the entry text to /output/entry.txt.

Python 3.13, standard library only, no network.
"""

# The entry is exactly one emoji, nothing else: a sunrise over the
# sea (U+1F305 SUNRISE), one character, four UTF-8 bytes — inside
# the gate's 1-to-8-character window, no words, no trailing newline.
# A dream vacation as a single postcard moment: dawn at a faraway
# shore, the whole trip ahead of it.
# Revision note: kept the entry to the single code point U+1F305 on
# purpose — no variation selector, so the text is 4 bytes and wins
# the smaller-text tie-break over multi-code-point emoji.
import os

TEXT = "\U0001F305"


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
