# Algebra I: the textbook

`algebra-1-book.tex` builds `algebra-1-book.pdf`: the lectures of Algebra I (Prof. Rahul
Pandharipande, ETH Zürich, fall 2026) ordered by topic and written as a book. The lecture
notes (`algebra-1.tex`, `content/`) stay the checked record of what was said and written. The
book is derived from them and then edited as text of its own; it is never regenerated.

Started on 2026-11-21 with Chapter 6 as the pilot. Chapters 0 to 5 are placeholders that hold
only the statements Chapter 6 cites.

## Build

```
latexmk -pdf algebra-1-book.tex
```

- The book reads the lecture notes' preamble: everything in `algebra-1.tex` before
  `\begin{document}` (see the comment at the top of `algebra-1-book.tex`). A change to that
  preamble therefore changes the book too: rebuild both PDFs in the same commit.
- `\booksourcestrue` in `algebra-1-book.tex` prints each section's sources (lecture and
  timestamps) in grey, for checking a passage against the lecture notes or the recording.

## Files

| File | What it is |
|---|---|
| `algebra-1-book.tex` | Main file: borrows the lecture preamble, then the book's parts and chapters |
| `book/book-preamble.tex` | What the book changes: "Chapter", numbered sections, headers, the *Beyond the Lecture* box, `\source{...}` |
| `book/frontmatter.tex` | Title page, contents, *About This Book* |
| `book/stub-ch00.tex`, `book/stubs-ch01-ch05.tex` | Placeholders (pilot) |
| `book/chNN-*.tex` | Written chapters |
| `tools/book/coverage.py` | Checks that a chapter keeps every labelled statement of its sources |

## How a chapter is written

1. **Sources.** The chapter names its lecture passages in `% SOURCE:` lines at the top
   (file | first line | end line, exclusive). Draft only from reviewed lectures.
2. **Statements** (definitions, theorems, examples, exercises) are copied from the board
   versions in the `content` boxes and changed only to unify notation. They keep their lecture
   labels, so references stay valid and coverage can be checked. A statement the lectures gave
   twice (a restatement at the start of the next lecture, `\recap`, `-wN` labels) appears once
   and carries both labels.
3. **Prose** is written fresh, in the voice of a book ("we"), never "the lecturer says". Speech,
   student exchanges and insight boxes are read for motivation and pictures only; nothing is
   quoted. No timestamps, `\inlinemetanote`, administrative notes, pauses or scratchpads.
4. **Notation** stays the lecturer's: a plain `m` for maximal ideals, a script `\mathscr{I}` for
   sets of ideals, `\subset` allowing equality, `\stackrel{\text{def}}{\iff}` and `:=` in
   definitions, and the board notation the lecture notes follow (units, content, ...).
5. **Additions** are marked. Mathematics the lectures did not give (a proof, a fact, an example)
   goes in `\begin{beyond}[Title] ... \end{beyond}`. Names and notations used in textbooks but
   not in the lectures (Krull's theorem, `\mathfrak{m}`, `C_c^\infty`) go in footnotes. AI notes
   of the lecture notes that are about the transcription itself are dropped.
6. **Sources per section:** `\source{W5 Tue 00:10:11--00:26:03}` after each `\section`.
7. **Checks** before committing:
   - `py -I tools/book/coverage.py book/<chapter>.tex` says OK;
   - grep the chapter for `inlinemetanote`, `speech`, `lecturer`, `\subseteq`, `---`;
   - the build is clean (no errors, no undefined references);
   - every figure is rendered and looked at.

## Outline and status

| Ch. | Title | From the lectures | Status |
|---|---|---|---|
| 0 | Background from the First-Year Courses | `content/prerequisites.tex` | placeholder |
| | **Part I: Rings** | | |
| 1 | Rings, Homomorphisms and Ideals | W1 Wed, W2 Tue | placeholder |
| 2 | The Language of Categories | W2 Tue, W2 Wed | placeholder |
| 3 | Integral Domains, Units and Divisibility | W2 Wed, W3 Tue | placeholder |
| 4 | Constructing Rings: Fractions, Polynomials, Power Series | W3 Tue, W3 Wed, W4 Tue | placeholder |
| 5 | Quotient Rings and the Correspondence Theorem | W4 Tue, W4 Wed, W5 Tue | placeholder |
| 6 | Maximal and Prime Ideals | W4 Wed, W5 Tue, Zorn outlook of W1 Wed | **written** (pilot, 2026-11-21) |
| 7 | The Chinese Remainder Theorem; Polynomial Rings over a Field | W5 Tue, W5 Wed | |
| 8 | Unique Factorization | W6 Tue | |
| 9 | Gauss's Theorem | W6 Wed, W7 Tue | |
| | **Part II: Groups** | | |
| 10 | Groups, Subgroups and Lagrange's Theorem | W7 Tue, W7 Wed, W9 Tue | |
| 11 | Homomorphisms, Normal Subgroups and Quotient Groups | W2 Tue, W8 Tue, W8 Wed, W9 Tue | |
| 12 | Conjugation and Automorphisms | W8 Tue, W8 Wed | |
| 13 | Group Actions and the Orbit-Stabilizer Theorem | W9 Tue, W9 Wed, W10 Tue | |
| 14 | Sylow's Theorems | W10 Wed | |
| 15- | Weeks 11 to 14 | | after the lectures |

**Chapter 0** needs its own adaptation pass: the prerequisites chapter of the lecture notes
points to about 50 lecture labels and says "Week n" 35 times. It is best done once the chapters
it points to exist.
