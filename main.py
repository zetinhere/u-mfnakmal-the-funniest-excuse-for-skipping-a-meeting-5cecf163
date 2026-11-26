#!/usr/bin/env python3
"""The Funniest Excuse for Skipping a Meeting — make.fun entry.

Writes one razor-sharp line (96 characters) to /output/entry.txt: the
funniest excuse for skipping a pointless work meeting.

Deterministic by design: a fixed string, no randomness, no clock, no
network, no input. Two runs produce byte-identical output.
"""

import os

ENTRY = "Sorry, I already attended this exact meeting in 2019. Nothing has changed, including the slides."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    print(ENTRY)


if __name__ == "__main__":
    main()
