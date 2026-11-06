# Second opinion on `findings.md`

Reviewed on 2026-11-06 against the git history of all 13 commits from `ad9d1d8` to `23824a0`.

## Scope and limits

- I read all 13 commit messages and the per-file `--numstat` for every commit.
- I read the diffs for `73ee610`, `c3d2d99` and the relevant parts of `12eeda7`, `8bfe02a`, `e751361`, `4c1d89a`, `48ea320` and `06640a1`.
- I traced where specific terms came from with `git log -S` and `git grep` at several commits.
- I did **not** read every changed line. The diff is about 2,400 changed lines.
- I could **not** check anything against the board frames or the audio and video. The recordings are not in the workspace.
  This covers every "the lecturer writes X on the board" claim, the timestamp settlements, and the "Cat / Ord / GCD / m is on the board" claims.
  I can only say what the commits did and what they said they did.

## Overall

`findings.md` is about right in direction and wrong or overstated in several details.
Its core point stands: part of the pendulum swing was real and was partly walked back in `23824a0`.
I'd correct the points below before relying on it.

## Claims that hold up

| Claim in findings.md | Result |
| :--- | :--- |
| 13 commits, 16 files, +1,242 / −1,228 | Correct. |
| `23824a0` quote about "no index" | Exact. |
| `c3d2d99` repaired the self-inflicted `class`/`coset` sentence | Correct. `73ee610` introduced "a *class* of $I$. The lecture does not use this word…" and `c3d2d99` fixed it. |
| `73ee610` replaced the field-norm argument with the lecturer's length argument | Matches the commit message. |
| `\mathcal{C}` → `\operatorname{Cat}` in the category definitions | Correct. The quoted LaTeX in `findings.md` matches the Week 2 Wednesday file exactly. |
| Monoid definition was deleted from `prerequisites.tex` | Correct, and the "Monoids are gone again" comment is in the file. |
| `R^\times` → `\mathcal{U}_R` | Correct. Occurrences of `R^\times` fell from 63 to 5 and `\mathcal{U}_R` rose from 20 to 79 in `48ea320`. |

## Where findings.md is wrong or overstated

1. **Wrong commit for the monoid deletion.**
   The definition was removed in `06640a1` ("definition signs… prerequisites"), not in `73ee610`.
   `73ee610` only names "monoid" in its message, and its diff does not touch the prerequisites.
   The recommendation to restore monoid is still right.
   It is also hidden inside a commit whose message says nothing about it.

2. **Wrong commit for the `\gcd` → `\operatorname{GCD}` change.**
   The count of `\operatorname{GCD}` went 29 → 33 in `73ee610` and 33 → 86 in `12eeda7`, and `\gcd` went 31 → 0.
   The bulk change, including `prerequisites.tex`, is in `12eeda7`.
   `findings.md` rates `12eeda7` as "Good" and calls the capitalised operators an overcorrection elsewhere.
   Those two verdicts contradict each other.

3. **"Purged" and "completely eradicated" the theorem names is overstated.**
   - "Correspondence Theorem" was never purged. It stayed in the Week 4 Wednesday chapter title, section titles, proof titles, and the Week 5 theorem title "Ideal Correspondence Theorem".
   - The "Krull's Theorem" aiNote already existed before today (`git log -S` finds no commit in the range that adds it). The name stayed in the text in an aiNote.
   - What `73ee610` removed was the names in the titles of four results (Frobenius Identity, Correspondence Theorem, Third Isomorphism Theorem, Krull's Theorem). `23824a0` put those back.
   - So it was a title-level swing with some names kept in aiNotes. It was not the "nearly unsearchable" document that `findings.md` describes.

4. **"Global search-and-replace to expunge coset" is not accurate.**
   `73ee610` created an `aiNote[Terminology: Cosets]` and moved the term there.
   It also wrote "Going beyond the lecture: … left coset…" for the left-coset remark.
   The coset term was relocated and labelled. The one broken sentence was a real blunder and was fixed.

5. **`\mathfrak{m}` → `m` is misdescribed.**
   `findings.md` says this happened in `73ee610` and `c3d2d99`. It happened only in `c3d2d99`. `73ee610` kept `\mathfrak{m}`.
   `c3d2d99` also changed the `writes:` notes, which are meant to record what the board shows.
   It added `aiNote[Notation: Maximal Ideals]` ("Many textbooks write … $\mathfrak{m}$. The lecturer writes a plain $m$ on the board…").
   So it is a documented fidelity change, not silent literalism.
   The clash with integer moduli (`ℤ/mℤ`) is still a fair readability point.
   Whether it is an overcorrection depends on whether the board really shows a plain `m`, which I cannot verify.

6. **The "35% / 35% / 30%" breakdown has no support.**
   Nothing in the repository gives those numbers. Delete it.

7. **Omissions.**
   - `48ea320` is dominated by Week 6 (46 + 90 changed lines) and also corrected nine `writes:` notes against frames.
     `findings.md` describes it mostly as notation substitution.
   - `7cc9e9a` / `06640a1` are described as "benign churn" and "standardising to `:=`".
     The messages say the opposite direction for some cases: "he writes def over = or a plain =, never :=".
     They follow the board, so they are not taste-driven consistency work.
   - `06640a1` is the commit that deleted the monoid definition, and its message is empty. That is the most consequential edit in that commit and it is not visible from the message.

## Where I agree with findings.md

- The monoid deletion from a chapter that says it is not a lecture transcript is the clearest mistake.
  I'd restore it.
- `\operatorname{Cat}` as a variable for an arbitrary category is confusing.
  The category-of-small-categories convention makes it worse. The Week 2 Wednesday file also writes `\widehat{\operatorname{Cat}}` for the second category in the functor definition.
  That depends on the board really showing "Cat", which I can't confirm.
- `23824a0` was the right correction.

## Suggested edits to findings.md

- Correct the commit attributions for the monoid deletion (`06640a1`) and the GCD capitalisation (`12eeda7`).
- Remove the 35/35/30 split.
- Rewrite section 1 and section 2 of "Did Claude overcorrect?" to say what `73ee610` actually did: title-level name removal, with names moved into aiNotes and `Going beyond the lecture:` markers.
- Note that the `\mathfrak{m}` change came with an explanatory aiNote and corrected the `writes:` notes.
- Add that none of the board-fidelity claims could be checked here.


---

# Addendum: reading the book itself (partial)

## What I read and what I did not

| Part | Status |
| :--- | :--- |
| `prerequisites.tex` | Read in full |
| Week 1 | Read in full, including speech blocks |
| Week 2 Tuesday and Wednesday | Read in full, speech blocks excluded |
| Week 3 Tuesday and Wednesday | Read in full, speech blocks excluded |
| Week 4 Tuesday | Read to about line 640 of 1453, speech blocks excluded |
| Rest of Week 4, Weeks 5 to 7 | **Not read** |
| All speech blocks from Week 2 on | **Not read.** They are verbatim transcript and I cannot check them without the recordings. |

I stopped because of the token limit. I extracted the non-speech parts into scratch copies to save tokens.

## Result for the parts I read

- **No mathematical errors found.** I checked the proofs and computations as I went.
  This covers the Euclidean algorithm numbers, the `(Z/4Z)[x]` unit `1+2x`, the `Z/6Z` equivalence counterexample, the power-series inverse, the totient counts and the dual-functor formulas.
- **Dates and attributions** checked out from memory: Higman and Neumann 1952, Kummer's ideal numbers in the 1840s, Dedekind 1872, the Swiss 10-franc banknote, and Erdős.

## Issues found

1. **`\operatorname{Cat}` is worse than findings.md says.**
   It is used in the category definition, the isomorphism definition, the functor definition and its figure, and the opposite-category note.
   The functor definition writes `\widehat{\operatorname{Cat}}` for the second category.
   Dropping the subscript from `Hom_C` also leaves `Hom(F(A),F(B))` and `Hom(A,B)` ambiguous in that definition.
2. **The monoid deletion is milder than I said earlier.**
   `prerequisites.tex` now defines a group directly, so the chapter is self-contained.
   The only loss is the remark that ring multiplication is a monoid.
   findings.md ranks this as the clearest mistake, and I would no longer call it that.
3. **Summaries in Weeks 1 to 3 were not audited like Weeks 4 to 7.**
   - The Week 3 Tuesday summary writes `N(a+bi)=a^2+b^2=1`, while an aiNote in the same file says the lecturer does not use `N`.
   - The Week 1 summary states "iff" and the `p = 2` case as lecture content. The lecture gave one direction and left out `p = 2`. The `p = 2` case is only in an aiNote.
4. **Week 1, line 1055** has an editorial "(it is the kernel of π…)" inside a speech block, but the map is called `f` in that lecture.
5. **Week 3 Tuesday:** "initial object among all field extensions" should say fields of characteristic 0.
6. **Week 2:** the category `Ring` is described as "rings with identity". The course convention is commutative rings with unit.

## Not checked

`\mathfrak{m}` versus `m` in Weeks 4 and 5, `\operatorname{GCD}` and `\operatorname{Ord}` in Weeks 6 and 7, and the remaining aiNotes and `Going beyond the lecture:` passages.
