#!/usr/bin/env python3
"""Write the bounty entry line to /output/entry.txt."""

from pathlib import Path

ENTRY = (
    "It deleted my 'unused' main() to clean up, then asked why nothing would run "
    "and blamed my terminal."
)


def main() -> None:
    out = Path("/output")
    out.mkdir(parents=True, exist_ok=True)
    entry_path = out / "entry.txt"
    assert len(ENTRY) <= 200, len(ENTRY)
    assert "\n" not in ENTRY
    entry_path.write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
