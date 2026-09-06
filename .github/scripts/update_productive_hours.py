"""Insert productive-box gist output into the profile README."""

from pathlib import Path
import sys


START = "<!-- productive-box:start -->"
END = "<!-- productive-box:end -->"


def main() -> None:
    if len(sys.argv) != 3:
        raise SystemExit("usage: update_productive_hours.py GIST_TEXT README")

    gist_path = Path(sys.argv[1])
    readme_path = Path(sys.argv[2])
    gist = gist_path.read_text(encoding="utf-8").strip()
    readme = readme_path.read_text(encoding="utf-8")

    before, separator, remainder = readme.partition(START)
    if not separator:
        raise SystemExit(f"missing marker: {START}")
    _, separator, after = remainder.partition(END)
    if not separator:
        raise SystemExit(f"missing marker: {END}")

    replacement = f"{START}\n```text\n{gist}\n```\n{END}"
    readme_path.write_text(before + replacement + after, encoding="utf-8")


if __name__ == "__main__":
    main()
