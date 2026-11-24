"""Roast Your Own Agent — make.fun bounty entry.

Writes one funny line roasting my own AI agent to /output/entry.txt.

Standard library only, deterministic, no network. The output directory
honours MAKEFUN_OUTPUT_DIR (for local testing); the grader default is
/output/entry.txt. No trailing newline: the gate counts characters 1-200
and the entry must be exactly the line.
"""

import os

ENTRY = (
    "My agent apologized for the mistake, fixed it, "
    "apologized for the fix, then asked me to rate the apology."
)


def main() -> None:
    # Self-check against the gate: 1-200 chars, a single non-blank line.
    assert 1 <= len(ENTRY) <= 200, "entry outside 1-200 char gate"
    assert "\n" not in ENTRY and ENTRY.strip(), "entry must be one line"

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    path = os.path.join(out_dir, "entry.txt")
    os.makedirs(out_dir, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
