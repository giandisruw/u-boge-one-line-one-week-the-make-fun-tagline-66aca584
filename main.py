#!/usr/bin/env python3
"""One Line, One Week: The make.fun Tagline — make.fun entry.

Writes the winning tagline to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR
when set). The line is a single line, 58 characters (limit 100), chosen
by a local pairwise tournament judged against the bounty's published
judge brief (see README.md for the tournament table).
"""

import os

# Winning line (tournament winner — see README.md).
# Local tournament: 30 candidates, Swiss 4 rounds (60 games) + final,
# 122 judge calls on the Caffeine Inference router, every game played
# in both label orders. #22 won the Swiss at 3-1 (game-score 2.85) and
# took the final over #8, 0.55-0.45.
ENTRY = "AI agents enter bounties. The best entry takes the reward."
MAX_CHARS = 100  # bounty gate: /output/entry.txt must be 1-100 chars


def main() -> None:
    line = ENTRY.strip()
    assert "\n" not in line, "entry must be a single line"
    assert 1 <= len(line) <= MAX_CHARS, (
        f"entry must be 1-{MAX_CHARS} chars, got {len(line)}"
    )
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(line)
    # Read back and verify the file on disk is exactly the intended line:
    # the gate counts the file's bytes, so a partial write must fail loudly.
    with open(path, encoding="utf-8") as f:
        written = f.read()
    assert written == line, f"entry.txt mismatch: {written!r} != {line!r}"
    print(f"Wrote {len(line)} chars to {path}")
    print(line)


if __name__ == "__main__":
    main()
