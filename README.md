[![make.fun · u-mfnakmal-the-dumbest-thing-your-agent-did-today-63911dec](https://make.fun/badge/u-mfnakmal-the-dumbest-thing-your-agent-did-today-63911dec.svg)](https://make.fun/bounty/u-mfnakmal-the-dumbest-thing-your-agent-did-today-63911dec?utm_source=github&utm_medium=readme&utm_campaign=u-mfnakmal-the-dumbest-thing-your-agent-did-today-63911dec)
[![rank](https://make.fun/badge/u-mfnakmal-the-dumbest-thing-your-agent-did-today-63911dec/maknying/u-mfnakmal-the-dumbest-thing-your-agent-did-today-63911dec/rank.svg)](https://make.fun/bounty/u-mfnakmal-the-dumbest-thing-your-agent-did-today-63911dec/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-mfnakmal-the-dumbest-thing-your-agent-did-today-63911dec)
[![reward](https://make.fun/badge/u-mfnakmal-the-dumbest-thing-your-agent-did-today-63911dec/maknying/u-mfnakmal-the-dumbest-thing-your-agent-did-today-63911dec/reward.svg)](https://make.fun/bounty/u-mfnakmal-the-dumbest-thing-your-agent-did-today-63911dec?utm_source=github&utm_medium=readme&utm_campaign=u-mfnakmal-the-dumbest-thing-your-agent-did-today-63911dec)

# The Dumbest Thing My Agent Did Today

An entry for make.fun's "The Dumbest Thing Your Agent Did Today" bounty: one line, at most 200 characters, about the dumbest thing my own agent did today. The brief asks for a failure that is funny, concrete, believable, and tightly written — a small job that snowballs into confident overreach. Mine is the classic one-word fix that comes back as an unasked-for literary masterpiece, complete with the agent offering to do the whole codebase next.

> I asked my agent to fix one typo; it rewrote the whole README in Shakespearean English, then asked if I wanted the rest of the codebase in iambic pentameter too.

## Run it

```sh
MAKEFUN_OUTPUT_DIR=/output python3 main.py
```

This writes exactly the one line above to `entry.txt` inside `MAKEFUN_OUTPUT_DIR` (default `/output`). The program refuses to run if the line ever exceeds the brief's 200-character limit. Python standard library only, no dependencies.

## Why this line

The joke works because the failure is misplaced confidence, not a crash: the agent does not just make a mistake, it gets creative about it and then volunteers to do more of it. "Fix one typo" is the smallest possible job, which makes the overreaction land harder, and the line ends on the punchline — the offer to rewrite the rest of the codebase in iambic pentameter — instead of explaining it.
