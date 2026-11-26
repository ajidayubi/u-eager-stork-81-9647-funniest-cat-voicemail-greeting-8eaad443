#!/usr/bin/env python3
"""Funniest Cat Voicemail Greeting — make.fun bounty entry.

Writes one voicemail greeting, recorded by a cat, to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output). Zero dependencies,
no time, no randomness, no network, no input: the same line every run.
"""

import os
import sys

LINE = "You've reached Miso. I'm asleep in the box your parcel came in. Leave a message — I'll knock it off the shelf at 4am."

MAX_CHARS = 120


def _validate(text):
    """Mirror the competition gate: 1-120 chars, non-whitespace UTF-8.

    Returns the entry encoded as UTF-8 bytes, so encoding happens in
    exactly one place and the writer cannot drift from the check.
    """
    if not isinstance(text, str):
        raise ValueError("entry must be text")
    if not (1 <= len(text) <= MAX_CHARS):
        raise ValueError(
            "entry must be 1-%d characters, got %d" % (MAX_CHARS, len(text))
        )
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    return text.encode("utf-8")


def main():
    data = _validate(LINE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    path = os.path.join(out_dir, "entry.txt")
    os.makedirs(out_dir, exist_ok=True)
    with open(path, "wb") as f:
        f.write(data)
    with open(path, "rb") as f:
        if f.read() != data:
            raise RuntimeError("entry.txt did not round-trip byte for byte")
    print(LINE)
    return 0


if __name__ == "__main__":
    sys.exit(main())
