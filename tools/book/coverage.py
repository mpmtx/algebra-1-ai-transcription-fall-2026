"""Check that a book chapter keeps every labelled statement of its lecture sources.

Usage (from the repository root):
    py -I tools/book/coverage.py book/ch06-maximal-and-prime-ideals.tex

The chapter names its sources in comment lines of the form
    % SOURCE: <lecture file> | <first-line marker> | <end-line marker>
A range runs from the first line that contains the first marker up to, not
including, the next line that contains the end marker. Every label in such a
range (except equation labels, eq:...) must be defined somewhere in the book,
that is in book/*.tex; a statement the lectures gave twice carries both labels
there. The report says where each label went. Exit code 1 if one is missing.
"""
import pathlib
import re
import sys

LABEL = re.compile(r"\\label(?:\[[^\]]*\])?\{([^}]+)\}")
SOURCE = re.compile(r"%\s*SOURCE:\s*(.+?)\s*\|\s*(.+?)\s*\|\s*(.+?)\s*$")


def read_lines(path):
    return path.read_text(encoding="utf-8", errors="replace").splitlines()


def labels(lines, first=0, last=None):
    """(label, line number) for each label outside comment lines."""
    found = []
    for k in range(first, len(lines) if last is None else last):
        line = lines[k]
        if line.lstrip().startswith("%"):
            continue
        for label in LABEL.findall(line):
            found.append((label, k + 1))
    return found


def source_range(path, start, end):
    lines = read_lines(path)
    i = next((k for k, line in enumerate(lines) if start in line), None)
    if i is None:
        sys.exit(f"{path}: start marker not found: {start}")
    j = next((k for k in range(i + 1, len(lines)) if end in lines[k]), None)
    if j is None:
        sys.exit(f"{path}: end marker not found after line {i + 1}: {end}")
    return i + 1, j, [(lab, n) for lab, n in labels(lines, i, j) if not lab.startswith("eq:")]


def main():
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    chapter = pathlib.Path(sys.argv[1])
    sources = [m.groups() for m in map(SOURCE.match, read_lines(chapter)) if m]
    if not sources:
        sys.exit(f"{chapter}: no '% SOURCE:' lines")

    defined = {}  # label -> book file
    for tex in sorted(pathlib.Path("book").glob("*.tex")):
        for label, _ in labels(read_lines(tex)):
            defined.setdefault(label, tex.name)

    missing = 0
    from_sources = set()
    for file, start, end in sources:
        first, last, found = source_range(pathlib.Path(file), start, end)
        print(f"\n{file}, lines {first}-{last}: {len(found)} labels")
        for label, line in found:
            from_sources.add(label)
            where = defined.get(label)
            if where is None:
                missing += 1
                print(f"  MISSING   {label}  (line {line})")
            elif where == chapter.name:
                print(f"  here      {label}")
            else:
                print(f"  {where}: {label}")

    new = [lab for lab, _ in labels(read_lines(chapter))
           if lab not in from_sources and not lab.startswith("eq:")]
    if new:
        print(f"\nNew labels of the book (not in the sources): {', '.join(new)}")
    print(f"\n{'OK' if not missing else f'{missing} label(s) MISSING'}")
    sys.exit(1 if missing else 0)


if __name__ == "__main__":
    main()
