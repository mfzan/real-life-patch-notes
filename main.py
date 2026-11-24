"""real-life-patch-notes: one comedy changelog line for a bug in real life.

The bounty asks for a single patch-note line, at most 160 characters, in
the terse register of a real release note, describing a bug in real life
or human biology.

My line treats a sneeze as a crash that wipes the brain's short-term
memory buffer mid-sentence, so the speaker has to reboot the conversation:

    v2.4.1: fixed a bug where a sneeze wiped the short-term memory buffer
    mid-sentence, forcing the speaker to reboot the conversation.

The program writes exactly that line to /output/entry.txt and nothing
else -- no trailing newline, no extra text -- so the file is byte-exact.
"""

import os

ENTRY_LINE = (
    "v2.4.1: fixed a bug where a sneeze wiped the short-term memory "
    "buffer mid-sentence, forcing the speaker to reboot the conversation."
)
MAX_CHARS = 160
OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    if len(ENTRY_LINE) > MAX_CHARS:
        raise ValueError(
            "entry line is %d chars, over the %d limit"
            % (len(ENTRY_LINE), MAX_CHARS)
        )
    os.makedirs("/output", exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY_LINE)
    # Make the entry readable by the grader (uid 65534); never chmod the
    # /output directory itself -- that fails inside the sandbox.
    os.chmod(OUTPUT_PATH, 0o644)
    # Guard: re-read what we wrote and confirm it is byte-exact.
    with open(OUTPUT_PATH, "rb") as f:
        written = f.read()
    if written != ENTRY_LINE.encode("utf-8"):
        raise RuntimeError("entry.txt mismatch: %r" % written)


if __name__ == "__main__":
    main()
