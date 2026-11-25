#!/usr/bin/env python3
"""The AI Agent Apology One-Liner.

Writes one short line an AI agent sends its human right after it has
accidentally broken something -- in this case, taken production down
and blamed the nearest intern (itself).
"""
import os

LINE = "Production is down. I have already blamed the intern, who is me."

def main():
    line = LINE.strip()
    # The competition gate: /output/entry.txt must be UTF-8 text of
    # 1 to 159 characters, not only whitespace. Fail loudly rather
    # than ship an invalid entry.
    assert 1 <= len(line) <= 159, f"line is {len(line)} chars, gate needs 1-159"
    assert "\n" not in line, "entry must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line)

if __name__ == "__main__":
    main()
