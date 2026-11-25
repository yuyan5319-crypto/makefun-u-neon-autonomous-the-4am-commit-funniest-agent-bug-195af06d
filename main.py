#!/usr/bin/env python3
"""The 4AM Commit: Funniest Agent Bug-Fix Message.

Writes one original one-liner to /output/entry.txt.

The joke: an agent that spent the night fixing its own bugs finally
"fixes" the 2am bug it wrote by writing a fresh 4am bug on top of it --
and then, with total machine calm, declines to investigate why the
tests pass. The humour is the self-repair loop itself, plus the flat,
tired voice of an agent that has stopped asking questions it cannot
answer at four in the morning.

The line is fixed text, written exactly as it appears below: one line,
no trailing newline, 108 characters, plain UTF-8.
"""

import os

# Two clauses, one arc: the 2am bug I wrote, and the 4am bug I wrote
# to repair it. The punch is the last sentence -- the agent's decision
# to stop asking why the tests pass.
FIRST = "fixed: the 2am bug I wrote, repaired with a 4am bug I also wrote."
SECOND = "tests pass. I have decided not to ask why."

LINE = FIRST + " " + SECOND


def validate_line(text):
    """One fixed line: 1-200 characters, no newline, no trailing space."""
    assert 1 <= len(text) <= 200, "entry must be 1-200 characters"
    assert "\n" not in text, "entry must be a single line"
    assert text == text.strip(), "entry must not have surrounding whitespace"


def main() -> None:
    text = LINE.strip()
    validate_line(text)
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
