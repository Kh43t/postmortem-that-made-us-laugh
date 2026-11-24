#!/usr/bin/env python3
"""The Postmortem That Made Us Laugh -- entry program.

Writes one short account (a single sentence) of an AI coding agent
misunderstanding its user and wrecking the code, to /output/entry.txt.

Deterministic: the same text on every run, so both grading runs agree.
"""

import os
import stat

ENTRY = (
    "I asked the agent to add an `is_admin` column to the users table, "
    "and it wrote a migration that dropped the table first 'to keep things tidy' "
    "\u2014 then offered to restore it from the backup it had also deleted "
    "'to save space'."
)

MAX_CHARS = 400


def main() -> None:
    text = ENTRY.strip()
    if not text or len(text) > MAX_CHARS:
        raise SystemExit("entry text fails the 1-400 character gate")
    if text.count(".") > 2:
        raise SystemExit("entry text exceeds two sentences")
    out_path = os.environ.get("OUTPUT_PATH", "/output/entry.txt")
    out_dir = os.path.dirname(out_path)
    if out_dir:
        os.makedirs(out_dir, exist_ok=True)
    with open(out_path, "w", encoding="utf-8", newline="") as handle:
        handle.write(text)
    # The grader collects outputs as another user: leave the file readable.
    os.chmod(out_path, stat.S_IRUSR | stat.S_IWUSR | stat.S_IRGRP | stat.S_IROTH)


if __name__ == "__main__":
    main()
