#!/usr/bin/env python3
"""Print the funniest sick-day excuse: one line, under 200 characters.

The excuse lives in entry.txt (exactly one line). This script prints it
after a deterministic self-check: length, single sentence, and a
read-back comparison against the embedded copy.
"""

import pathlib
import sys

ENTRY = "I pulled a muscle reaching for the snooze button, and my doctor says the only cure is a full day of not reaching for anything."


def self_check(entry: str) -> None:
    """Validate the gate: one line, one sentence, under 200 characters."""
    assert entry == entry.strip(), "entry has leading/trailing whitespace"
    assert "\n" not in entry and "\r" not in entry, "entry spans more than one line"
    assert 0 < len(entry) < 200, f"entry is {len(entry)} chars, must be under 200"
    sentence_enders = sum(entry.count(mark) for mark in (".", "!", "?"))
    assert sentence_enders == 1, f"entry has {sentence_enders} sentences, must be 1"
    assert entry[0].isupper(), "entry must start with a capital letter"


def main() -> int:
    entry_path = pathlib.Path(__file__).with_name("entry.txt")
    on_disk = entry_path.read_text(encoding="utf-8").strip()
    assert on_disk == ENTRY, "entry.txt does not match the embedded excuse"
    self_check(ENTRY)
    print(ENTRY)
    return 0


if __name__ == "__main__":
    sys.exit(main())
