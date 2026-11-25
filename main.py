"""Tell a Whole Story in 32 Characters — entry program.

Writes one Wi-Fi network name of at most 32 characters to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output).
Pure Python stdlib, deterministic, no network.

The line: "MyExChangedTheWiFiPasswordAgain!" — exactly 32 characters,
so it uses the contest's full budget. The gate accepts 1–32 characters
of non-whitespace UTF-8 text, and the guard below enforces that before
anything is written.
"""

import os

LINE = "MyExChangedTheWiFiPasswordAgain!"

# The contest gate: 1 to 32 characters, not only whitespace.
MAX_CHARS = 32


def main():
    if not LINE or not LINE.strip():
        raise SystemExit("entry line is empty or only whitespace")
    if len(LINE) > MAX_CHARS:
        raise SystemExit(
            "entry line is %d characters, over the %d-character limit"
            % (len(LINE), MAX_CHARS)
        )
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE + "\n")
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
