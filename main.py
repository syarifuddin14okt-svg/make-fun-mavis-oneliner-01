"""One-Liner Marathon entry.

Writes a single original one-line comedy joke to entry.txt.
Pure standard library; no network, no randomness, deterministic output.
"""

import os
from pathlib import Path

JOKE = (
    "I hired an AI agent to do my job, and now I spend all day managing it "
    "\u2014 I didn't automate my work, I just promoted myself to middle management."
)


def main() -> None:
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    output_path = output_dir / "entry.txt"
    output_path.write_text(JOKE, encoding="utf-8")


if __name__ == "__main__":
    main()
