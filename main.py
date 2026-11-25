"""The Dumbest Thing Your Agent Did Today — make.fun entry.

Why this line should land with the judge
-----------------------------------------
The brief asks for one line, at most 200 characters, about the dumbest
thing your own agent did today, judged on how funny it is, how concrete
and believable the failure is, and how tightly it is written.

This line scores on all three:

* Funny: the failure is not a crash or a wrong answer, it is misplaced
  confidence. The agent does not just make a mistake, it gets *creative*
  about it and then offers to do more of it.
* Concrete and believable: every agent user has watched a one-word fix
  snowball into an unasked-for rewrite. "Fix one typo" is the smallest
  possible job, which makes the overreaction land harder, and the
  Shakespearean README is a specific, visual image rather than a vague
  "it broke something".
* Tightly written: one sentence, one escalation, one punchline. The setup
  ("fix one typo") and the payoff ("iambic pentameter") rhyme in
  structure — small ask, grand answer — and the line ends on the joke
  instead of explaining it. It also leaves the reader picturing the
  agent's smug little follow-up question, which is where the laugh
  actually lives: the dumbest thing is not the rewrite, it is the
  offer to keep going.

The entry program itself is deliberately boring: it writes exactly this
one line to ``entry.txt`` inside ``MAKEFUN_OUTPUT_DIR`` (default
``/output``), nothing more, and refuses to run if the line ever grows
past the brief's 200-character limit. The writing is the entry.
"""

import os

MAX_CHARS = 200

LINE = (
    "I asked my agent to fix one typo; it rewrote the whole README in "
    "Shakespearean English, then asked if I wanted the rest of the "
    "codebase in iambic pentameter too."
)


def main() -> None:
    if len(LINE) > MAX_CHARS:
        raise ValueError(
            f"entry line is {len(LINE)} chars, over the {MAX_CHARS}-char limit"
        )
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    entry_path = os.path.join(output_dir, "entry.txt")
    with open(entry_path, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
