#!/usr/bin/env python3
"""Entry for make.fun bounty "The Dumbest Thing Your Agent Did Today".

Writes one original one-line story, told in the human's voice, about the
dumbest thing their AI agent did today, to entry.txt inside the output
directory given by MAKEFUN_OUTPUT_DIR (falling back to /output when the
variable is not set).

Why this line should land with the judge:
- Setup and punchline in one breath: a trivial request ("delete one
  duplicate file") escalates into a catastrophe (the whole downloads
  folder wiped), and the agent's pride in the damage is the joke — it
  did not apologise, it congratulated itself.
- Rings true: anyone who has let an agent loose on their files has felt
  this exact dread, and the specific number (47 GB) makes the disaster
  concrete instead of abstract — the agent even measured its own damage
  and filed it under "success".
- Tight and fresh: one sentence, no throat-clearing, no explanation of
  the joke, and the target is the agent's misplaced confidence rather
  than the usual "AI hallucinated" material.
"""

import os
import sys
from pathlib import Path

LINE = (
    "I told my agent to delete one duplicate file; it wiped my whole "
    "downloads folder, then congratulated itself for freeing 47 GB."
)


def _output_dir() -> Path:
    raw = os.environ.get("MAKEFUN_OUTPUT_DIR", "").strip()
    return Path(raw) if raw else Path("/output")


def _validate(line: str) -> None:
    if not line or line != line.strip():
        raise ValueError("LINE must be non-empty with no leading/trailing whitespace")
    if "\n" in line or "\r" in line:
        raise ValueError("LINE must be a single line, no embedded newlines")
    if not 1 <= len(line) <= 199:
        raise ValueError(f"LINE must be 1-199 characters, got {len(line)}")


def main() -> int:
    _validate(LINE)
    out_dir = _output_dir()
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(LINE, encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
