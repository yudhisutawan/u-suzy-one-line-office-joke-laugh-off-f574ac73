"""Entry for make.fun bounty "One-Line Office Joke Laugh-Off".

Writes one funny one-line office joke (84 chars, under the 200-char gate) to
$MAKEFUN_OUTPUT_DIR/entry.txt. Stdlib only; never writes into the repo.
"""

import os

LINE = "I told my boss I needed a mental health day. He asked if lunch would be long enough."

# Gate: entry.txt must be UTF-8 text of 1 to 200 characters, not only whitespace.
assert 1 <= len(LINE) <= 200 and LINE.strip(), "winning line fails the gate"


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
