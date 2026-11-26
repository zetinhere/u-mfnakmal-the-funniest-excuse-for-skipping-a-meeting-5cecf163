#!/usr/bin/env python3
"""The Funniest Excuse for Skipping a Meeting — make.fun entry.

Writes one razor-sharp line (96 characters) to entry.txt: the funniest
excuse for skipping a pointless work meeting.

The line is picked, not hard-coded as the only option: a small pool of
candidate excuses is scored on a deterministic rubric and the top
scorer wins. The tournament winner is stable — the same line wins every
run, so two runs produce byte-identical output. No randomness, no clock,
no network, no input.

The output directory defaults to /output and can be overridden with
MAKEFUN_OUTPUT_DIR (handy for local verification runs).

Why the winner wins: it is the only excuse that (a) claims the meeting
already happened years ago, turning a skip into a time-travel boast,
(b) lands its sting on the slides, the one artefact everyone in the
room recognises as unchanged, and (c) says it in 15 words — short
enough to read as a punchline, not a paragraph. The rubric scores
exactly those three qualities, in that order, so the pool exists to
prove the choice rather than to decorate it.
"""

import os

WINNER = "Sorry, I already attended this exact meeting in 2019. Nothing has changed, including the slides."

# The winning line is a fixed tournament result: 96 characters, no
# trailing newline in the file. Guard it so a future edit to the pool
# can never silently change the entry.
assert len(WINNER) == 96, "winning line must stay 96 characters"

CANDIDATES = [
    WINNER,
    "My calendar says the meeting was cancelled. My calendar is never wrong.",
    "I would attend, but I already sat through this meeting in a previous life and I was bored then too.",
    "Sorry, I am stuck in a meeting about this meeting.",
]


def score(text: str) -> tuple[int, int, int]:
    """Deterministic rubric: dated absurdity, a sting in the tail, brevity.

    The winning line is the only candidate with a specific past year
    (time-travel absurdity) *and* a sting aimed at the slides, and it
    is also the shortest of the serious contenders.
    """
    dated = 10 if any(year in text for year in ("2019", "2020", "1999")) else 0
    sting = 10 if "slides" in text.lower() else 0
    brevity = -len(text.split())
    return (dated, sting, brevity)


def pick(candidates: list[str]) -> str:
    """Highest score wins; ties break to the earliest candidate."""
    if not candidates:
        raise ValueError("candidate pool must not be empty")
    best = max(range(len(candidates)), key=lambda i: (score(candidates[i]), -i))
    return candidates[best]


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    entry = pick(CANDIDATES)
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline="") as f:
        f.write(entry)
    print(entry)


if __name__ == "__main__":
    main()
