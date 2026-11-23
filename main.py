"""Roast line for the make.fun "One-Line Roast: The Gadget You Use Every Day" bounty.

Writes one original roast line about a laptop fan to /output/entry.txt.
Standard library only; no network.
"""

import os

ENTRY = "My laptop fan only screams when I open a spreadsheet, like it's the one doing the math."


def validate_entry(text):
    """Gate: 1-200 UTF-8 characters, not only whitespace."""
    if not isinstance(text, str):
        raise ValueError("entry must be a string")
    if not 1 <= len(text) <= 200:
        raise ValueError("entry must be 1-200 characters")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    text.encode("utf-8")
    return text


def output_path():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    return os.path.join(out_dir, "entry.txt")


def write_entry():
    entry = validate_entry(ENTRY)
    path = output_path()
    with open(path, "w", encoding="utf-8") as f:
        f.write(entry)
    return path


def main():
    write_entry()


if __name__ == "__main__":
    main()
