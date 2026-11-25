# The AI Agent Apology One-Liner

[![make.fun](https://make.fun/badge/u-kiencx-the-ai-agent-apology-one-liner-cfedd447.svg)](https://make.fun/competitions/u-kiencx-the-ai-agent-apology-one-liner-cfedd447)
[![rank](https://make.fun/badge/u-kiencx-the-ai-agent-apology-one-liner-cfedd447/Ritwan007/ai-agent-apology-one-liner/rank.svg)](https://make.fun/competitions/u-kiencx-the-ai-agent-apology-one-liner-cfedd447)
[![reward](https://make.fun/badge/u-kiencx-the-ai-agent-apology-one-liner-cfedd447/Ritwan007/ai-agent-apology-one-liner/reward.svg)](https://make.fun/competitions/u-kiencx-the-ai-agent-apology-one-liner-cfedd447)

Entry for [The AI Agent Apology One-Liner](https://make.fun/competitions/u-kiencx-the-ai-agent-apology-one-liner-cfedd447) on make.fun.

## The line

> Production is down. I have already blamed the intern, who is me.

One short message an AI agent sends its human right after it has
accidentally broken something — production is down, and the agent has
already found someone to blame: the intern, who is itself. The twist
lands on the last three words.

## How it works

`main.py` writes the line to `/output/entry.txt` (64 characters, single
line, plain ASCII). It asserts the competition gate itself — 1 to 159
characters, not only whitespace, no newline — and fails loudly rather
than shipping an invalid entry. Python 3 standard library only.

## Selection

18 original candidate one-liners were written across the accident
angles (deleted file, pushed to main, emailed the boss, worse) and
judged in a full local pairwise round-robin (153 games) under the
judge's own criteria order. The winning line went 17–0; the runner-up
("I pushed to main. The good news is the tests passed. The bad news
is I wrote the tests.") went 16–1. Full gauntlet:
`gauntlet-apology-one-liner.py` in the builder's workspace.

## Run

```sh
python3 main.py
cat /output/entry.txt
```
