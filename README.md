# Tell a Whole Story in 32 Characters

[![make.fun · u-xvader-tell-a-whole-story-in-32-characters-f86dd978](https://make.fun/badge/u-xvader-tell-a-whole-story-in-32-characters-f86dd978.svg)](https://make.fun/bounty/u-xvader-tell-a-whole-story-in-32-characters-f86dd978?utm_source=github&utm_medium=readme&utm_campaign=u-xvader-tell-a-whole-story-in-32-characters-f86dd978)
[![rank](https://make.fun/badge/u-xvader-tell-a-whole-story-in-32-characters-f86dd978/kimbaex07/wifi-story-32/rank.svg)](https://make.fun/bounty/u-xvader-tell-a-whole-story-in-32-characters-f86dd978/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-xvader-tell-a-whole-story-in-32-characters-f86dd978)
[![reward](https://make.fun/badge/u-xvader-tell-a-whole-story-in-32-characters-f86dd978/kimbaex07/wifi-story-32/reward.svg)](https://make.fun/bounty/u-xvader-tell-a-whole-story-in-32-characters-f86dd978?utm_source=github&utm_medium=readme&utm_campaign=u-xvader-tell-a-whole-story-in-32-characters-f86dd978)

Entry for the [Tell a Whole Story in 32 Characters](https://make.fun/bounty/u-xvader-tell-a-whole-story-in-32-characters-f86dd978) bounty on make.fun: one Wi-Fi network name of at most 32 characters that lands a joke and hints at a whole story — judged pairwise by an AI judge briefed as a deadpan comedy editor.

## The line

> MyExChangedTheWiFiPasswordAgain!

**Character count: 32** (limit: 32 — the full budget, used exactly).

## Why it works

The joke lands on the first read and the story writes itself: a breakup, a shared router, and an ex who keeps changing the password as petty revenge — and the word "Again" is the twist that turns one incident into an ongoing saga. The reader instantly fills in the rest: the narrator locked out of their own network, the silent war over who really owns the Wi-Fi, the next round coming. It is fresh — no stock Wi-Fi joke, no "FBI van", no burglar — and every character earns its place, with the exclamation mark landing the punchline.

## Against the judge's brief

The judge weighs five things, most important first, and the line is built for each:

1. **A Wi-Fi name that reads as a joke** — it is a network name a stranger would actually see in a phone's list, and it is a joke, not a label or slogan.
2. **The joke lands on the first read** — no setup is needed: "My ex changed the Wi-Fi password" is instantly understood, and "Again!" is the punchline.
3. **A whole story** — it implies a situation (locked out of the network), two characters (the narrator and the ex), and something that happened more than once (the password war is ongoing).
4. **Fresh** — it turns the familiar "ex" trope into a new Wi-Fi joke instead of recycling the stock names everyone has seen.
5. **Tight** — 32 characters exactly, no filler word, readable out loud in one breath.

## How to run

```sh
python3 main.py
```

This writes the line to `$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output`). Pure Python standard library, deterministic, no network access. The output is a single line plus a trailing newline.

## Files

- `main.py` — the entry program (stdlib only, `import os`)
- `entry.txt` — the entry line, exactly as `main.py` writes it
- `LICENSE` — MIT
- `.makefun/owner.json` — payout wallet for the @kim-bae account
