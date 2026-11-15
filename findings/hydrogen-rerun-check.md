# Hydrogen XHIGH rerun of the group chapters: what survived from the reviews

Checked 2026-11-15 by Claude (Opus 5.5). Question: did the Hydrogen XHIGH rerun (`386fb16`, and
`3947fad` for Week 9 Tuesday) lose content that earlier reviews had checked against the board
frames, or introduce errors? Argon's own account of the rerun is in `group-chapters-audit.md`.

## Short answer

Argon's "restored most / all" does not hold. The big, visible fixes came back (Ramanujan
corrections, `Sign`, ⊂ in notes, the five knights, the normality proof, Lycka's name, the `n − r`
slip, Week 9 Tuesday's φ, hats and red crosses), but some 40 smaller frame-checked corrections did
not (section B), mostly in Weeks 7–8: arrows the board does not have are back, `CASE (i)`, `CONTRA`, `Part(n)`,
`φ̃`, `bij`, `Remember the ∼_N`, the `Φ_mat` check, `c_z` (now `C_z` everywhere), `Ord` (now `ord`
everywhere). Three notes are new inventions that today's frames contradict, two of them with an
aiNote that passes the invention on to the reader (`R^*` in Week 7 Tuesday; `H < G` in Week 9
Tuesday; a transitivity "slip" in Week 7 Wednesday).

Mathematics: nine problems in boxes and aiNotes (A1–A9). The one that matters most is A1: the
First Isomorphism Theorem box of Week 8 Tuesday states `G/ker(f) ≅ Im(f)` with `G` undefined. The
others are a wrong step in a short proof (A6), a wrong count rule as literally stated (A2), a false
"because" (A3), loose notation in boxes (A4, A5, A7, A9) and a box that displays a false formula
(A8). The reviewed proofs I checked are otherwise sound, and the figures are clean.

In three places `HEAD` is right and the earlier text was wrong (frames today): "because of dim
theory" (Week 9 Tuesday), `x ∼ y ⟺ xh = y for some h ∈ H` (Week 7 Wednesday), `(x² = −1)` (Week 9
Wednesday).

Line numbers are those of `HEAD` (`386fb16`). Chapters:

| Short | File | Baseline compared against |
|---|---|---|
| 10-27 | `content/step4-2026-10-27-tuesday-week7-…` | `f68edb4` (Flash base, reviewed 10-30 to 11-13) |
| 10-28 | `content/step4-2026-10-28-wednesday-week7-…` | `f68edb4` |
| 11-03 | `content/step4-2026-11-03-tuesday-week8-…` | `f68edb4` (frame review `4d7469b`) |
| 11-04 | `content/step4-2026-11-04-wednesday-week8-…` | `f68edb4` (frame review `2888d90`) |
| 11-10 | `content/step4-2026-11-10-tuesday-week9-…` | `d076faf` (frame review; the Hydrogen base came in `3947fad`) |
| 11-11 | `content/step4-2026-11-11-wednesday-week9-…` | `f68edb4` (never frame-reviewed) |

## How it was checked

1. For each reviewed chapter, every board note the reviews changed (raw pipeline commit → reviewed
   state) was paired with its nearest note in `HEAD` by text and timestamp, and read side by side
   (11-03: 55 corrected notes, 11-04: 31, 10-27/10-28: the frame commits `8379ef4`, `25cc4e4`,
   `ea08c7a`, `48ea320`, `8bfe02a`, `12eeda7`, `73ee610`; 11-10: 83).
2. The board conventions settled from frames (memory notes of 11-06/07/11) were counted in notes and
   boxes, before and after.
3. The fixes listed in the review commit messages were looked up one by one.
4. Board claims where `HEAD` and the earlier text disagree and it matters were settled with eight
   new frames (Week 7 Tue 00:37:10; Week 7 Wed 00:18:52, 00:24:42; Week 9 Tue 00:09:48, 00:24:14,
   00:39:54, 01:14:34; Week 9 Wed 00:09:14).
5. Math: my own reading of the statements and proofs the reviews had fixed, plus an independent
   read of each chapter by Gemini (section F); every Gemini finding used here was checked.
6. Figures: all of them rendered from the committed PDF (section D).

Not covered: notes the reviews had confirmed unchanged were only spot-checked where `HEAD` differs;
Week 9 Wednesday has no frame-checked baseline, so its notes are not judged here.

## A. Mathematics

**A1. 11-03, First Isomorphism Theorem box states `G/ker(f) ≅ Im(f)` (L1784–1789).** `G` is not
defined there; the theorem is about `f: G_1 → G_2`. The board slip `G` for `G_1` moved from the
note into the formal statement, and an aiNote (L1794) calls it "board shorthand". Before
(`f68edb4` L1815–1819): `G_1/ker(f) ≅ Im(f)`, and the note marked the slip. The same slip is in the
normality proof's box, "let `x ∈ G` and `n ∈ ker(f)`" (L1366–1368; `f68edb4` L1345: `x ∈ G_1`).
The summary (L2428) has it right.

**A2. 10-28, face-counting rule (L1056):** `|Rot(P)| = (in-plane symmetries of one face) × (number
of faces)`. The in-plane symmetries of a regular k-gon are 2k (with reflections); the rule needs the
k rotations, as the sentence just before says and as `f68edb4` L1030 had ("rotational symmetries
preserving a chosen face"). Read literally it gives 48 for the cube. [found by Gemini, checked]

**A3. 10-28, aiNote L1308:** "Because |S_8| = 8! = 40320, the homomorphism Rot(cube) → S_8 … is
injective". The size of S_8 does not make anything injective; the reason in brackets (a rotation
fixing all 8 vertices is the identity) is the real one. `f68edb4` L1273 used 40 320 ≫ 24 for what it
does show: the image is a tiny subgroup. [Gemini, checked]

**A4. 10-28, box L875:** `S_n ⟷ Partitions`. The bijection is between the conjugacy classes of
S_n and the partitions of n; `f68edb4` had `S_n / conjugacy ⟷ Partitions(n)`. (On the board he
writes `S_n ⟷ Part(n)` as a slogan, which the note may keep; the box should not.) [Gemini, checked]

**A5. 10-28, one symbol for two maps:** `φ` is the cube map `Rot(cube) → S_4` (L1202) and again the
tetrahedron map `Rot(tetrahedron) → S_4` (L1284, L1294). The board has `φ̃` for the second (see B).

**A6. 11-04, injectivity of `C_z` (L611–613):** `z x z⁻¹ = e ⟹ z x = z ⟹ x = z⁻¹ e z = e`. The
last step does not follow from `z x = z` (that gives `x = z⁻¹ z = e`); `f68edb4` L651 had it right.
[Gemini, checked]

**A7. 11-04, cycle decomposition box (L852):** `σ ⟼ (a_{11}, a_{12} … a_{1k_1})(a_{21}, …) …`. In
the box this must be `σ = (a_{11} a_{12} … a_{1k_1}) …` (equality, and no commas inside cycles, as
everywhere else in the book); `f68edb4` L923 had that. The board's `σ ↦` belongs in the note only.
[Gemini, checked]

**A8. 11-04, a box displaying a false formula (L1029–1034):** a `content` box "Board Prompt on the
Sign of σ" shows `Sign(σ) = n − r` with a red "(Incorrect …)". The slip is already in the note and
explained in the aiNote; `f68edb4` kept it out of the boxes. Not an error the reader can miss, but
the book's rule is that boxes state only correct mathematics.

**A9. 10-27, exercise box (L262–271) and summary (L2004):** "if `f ∈ I` has minimal lowest degree
`min`, then `I = (x^{\min})`". `min` is used as a number; `f68edb4` had `I = (x^m)` with `m` the
minimal degree, and the note `(x^m)` (L254 now also says `(x^{\min})`). [Gemini, checked]

Minor, wording: 11-11 L250 says `G` is "canonically" isomorphic to a subgroup of `Sym(G)` "(and
hence of `S_{|G|}`)"; the second embedding needs a numbering of `G` and is not canonical. 11-04
L998 puts braces around "Set of equiv. classes …" (a set whose one element is that set); harmless.

Checked and correct in `HEAD`: the Ramanujan box (`p(7k+5)`, `p(11k+6)`) and its aiNote on both
corrections (11-03 L2406–2420); the injectivity of `Rot(cube) → S_4` (10-28 L1207–1219, a new
proof, sign argument with `det(−I) = −1`, numbers verified); the group axioms numbered (G1)–(G3) and
cited consistently (10-27); `x ↦ −x` on `Z/nZ` non-inner only for `n ≥ 3` (11-04 L750–760); the
sign formula and the board slip `Sign(σ) = n − r` kept as a slip (11-04 L1027, L1039–1046); the
quotient-group theorem and axioms (11-03 L1491, L1685); `Aut(S_n)` and the `S_6` exception
(11-04 L801).

## B. Board fidelity: frame-checked corrections lost in `HEAD`

Frame evidence is from the review named in brackets; "re-confirmed" means a frame taken today.

### 10-27 (Week 7 Tuesday)
- `CASE (i)` / `CASE (ii)` are back to `Case (1)` / `Case (2)` (L433, L435) [`ea08c7a`].
- Red `CONTRA` became "writes \qt{contradiction} and crosses out that branch" (L685), and the red
  `(Ass f ∉ (p))` beside it is gone [`ea08c7a`; re-confirmed, frame 00:37:10].
- **New invented note:** "with `R^*` (meaning 0 ≠ m ∈ R) below m" (L741), and an aiNote (L761) that
  tells the reader the lecturer writes `R^*` there. The frame (00:37:10) shows `≠ 0` under `m` in
  `p | m·g`, `0 ≠` beside `m·g`, and `0≠R` with an arrow to `m` on the left. No `R^*`.
- The S₃ order lines have implication arrows again: `(1 2) ≠ e ⟹ ord ≠ 1`,
  `(1 2)(1 2) = e ⟹ ord = 2` (L1861); `8379ef4` had removed them ("no arrow at all … the
  (1 2) lines"), and `e → Ord(e) = 1` is now split into `e ⟶` and `ord(e) = 1`.
- `Ord(x)` → `ord(x)`: boxes 25 → 0, notes 5 → 2 (e.g. L1859, L1896). The board writes `Ord`
  (frames 2026-11-06, `73ee610`); Argon unified to `ord` on purpose and deleted the remark.
- Minor (descriptive): `circles B g p` → `points at` (L741).
- `(i) x, x², x³, …` → `(1)` (L1785) [`ea08c7a`]; `(1 2)(1 2) = e  ord : 2` → `⟹ ord = 2` and
  `ord = 3` → `3.` (L1861, L1865) [`8379ef4`]. [Gemini, checked against the reviewed text]
- The field is `k` in the book from Week 5 on (memory, 2026-11-06: his K and k are one chalk shape,
  the book unified it); `HEAD` has `K[[x]]` 25 times and `k[[x]]` 0 times (before: 0 and 18).
- The reviewed aside on Gauss's 1801 work (`3973234` made it accurate) is gone; only a recap is left
  (L306). An addition, so no loss of lecture content.

### 10-28 (Week 7 Wednesday)
- The tetrahedron map is `φ̃` on the board (frame 00:43:40); `HEAD` writes `φ` in the note (L1233)
  and the boxes (L1284).
- `S_n ⟷ Part(n)` became `S_n ⟷ Partitions` (L820) [`ea08c7a`].
- Symmetry row: `• x ∼ y then y ∼ x` became `• x ∼ y ⟹ y ∼ x`, and `⟺ xh = y` became
  `x ∼ y ⟹ xh = y` (L432) [`8379ef4`; re-confirmed, frames 00:18:52 and 00:24:42].
- **New invented slip:** transitivity is noted as `If x ∼ y ⟹ y ∼ z ⟹ x ∼ z`, "using ⟹ between the
  two hypotheses as a slip for and" (L453). The board says `If x∼y and y∼z ⟹ x∼z` (frame 00:18:52),
  as `f68edb4` had.
- The long diagonals are small `a, b, c, d` on the board (frame 00:43:40, memory); `HEAD` labels them
  `A, B, C, D` (L1107) and uses them in the box (L1203).
- S₃ examples: `(1 2)(3) ⇝ ord = 2`, `(1 2 3) ⇝ ord = 3` lost their wavy arrows (note L292; the box
  L304 has `⟹` again) [`8379ef4`, `879b9b6`].
- `G ∋ x h_1 = x h_2` lost `G ∋` (L677) [`ea08c7a`] (minor).
- `Ord` → `ord`: boxes 25 → 0, notes 8 → 3; the aiNote on his `Ord`/`ord` is gone. Re-confirmed:
  the frame at 00:18:52 shows `(12)(3) ⇝ Ord = 2`, `(123) ⇝ Ord = 3` and `does Ord(x) | |G|?`.
- One point for `HEAD`: `x ∼ y ⟺ xh = y, some h ∈ H` (L609) matches the board ("for some h ∈ H",
  frame 00:24:42); `f68edb4` had `∃ h ∈ H s.t.`.
- Kept: the angle-bracket slip `⟨e, x, …⟩` (L163, aiNote L182), transitivity `x h_1 h_2 = z`
  (L453), the invented `3·8 = 24` note stays out.

### 11-03 (Week 8 Tuesday)
- `Remember the ∼_N` (00:55) is not in the notes (speech L1510) [`4d7469b`].
- `bij` over the JNF arrow is gone from the note (L2108) and the box (L2116) [`4d7469b`].
- The `Φ_mat` homomorphism check: the board's `(Φ_mat(σ))(v_i)` that he crossed out is now an
  uncrossed note (L335); `≝ v_{σ̂σ(i)}` became `v_{(σ̂∘σ)(i)}` (L353); `= Φ_mat(σ̂) v_{σ(i)}` is
  back to the pre-review `Φ_mat(σ̂)(v_{σ(i)})` (L355); `def ∘ in S_n` over the double arrow is gone
  [`4d7469b`].
- The `G/ker(f)` note no longer says it is a slip (see A1).
- `Rot(△)` (a drawn tetrahedron) is `Rot(Δ)` in notes and boxes (L1034–1067); memory: boxes write
  `Rot(Tetrahedron)`, as Week 7 did.
- `you check` (pre-review form) instead of `You can check` (L703); `\square` → `\underline{\ }` in
  `1 + 6 + 3 + 8 + □ = 24` (L920); `Sign: S_n → {±1}` now drawn as `S_n —Sign→ {±1}` (L603,
  unverified) (all minor).
- The `% [WORD-CHECKED …]` comment (clip heard by the user: he says 7k + 6) is gone; the speech
  still says 7k + 6, correctly.
- Kept: `Sign` throughout, ⊂ in all notes, `def` over `=`, the five knights A–E, the normality proof
  ending `f(x x⁻¹) = f(e_1) = e_2`, `(GL_n(ℂ), ·, Id)`, both Ramanujan corrections.

### 11-04 (Week 8 Wednesday)
- `c_z` → `C_z` everywhere: notes 12 → 0, boxes 71 → 1 [`2888d90`, frames]. The aiNote at L160 even
  says textbooks write `c_z`. Argon's audit calls `C_z` "accurately distinguished"; the board has
  lowercase.
- `z ⟶ c_z` (plain arrow) is `z ⟼ C_z` again (L638, box L663) [`2888d90`: "no mapsto"]; same for
  `q: x ⟶ x̄` → `q: x ⟼ x̄` (L129).
- `(Every subgroup of abelian group is Normal)` became "Any subgroup of abelian group is normal"
  (L513).
- The board's `−1^{(k_1−1)}`, `−1^{(k_2−1)}` above the cycles became the tidy `(−1)^{k_i−1}`
  (L1056), and the aiNote (L1039) now says he wrote the base `(−1)` above each cycle.
- Minor (descriptive): the circle around `z⁻¹z` and the check mark (now `⟹ x = e`, L588).
- Notes the review had kept (so confirmed against frames) that `HEAD` now writes differently, not
  re-checked today: `c_z(xy) = c_z(x) c_z(y)` → `C_z(xy) ≟ C_z(x)·C_z(y)` (L572);
  `z x z⁻¹ z y z⁻¹` (circled `z⁻¹z`) → with `\cancel` strokes (L574); commas inside the cycles
  `(a_{11}, a_{12} …)` (L825); braces around "Set of equiv. classes …" (L987). [Gemini]
- Kept: Lycka's name (L470, L476), the `ker(f) ⊂ G` slip, `(G_1/ker f, ·, ē_1)`, the `≀` arrow,
  `G ⇝ Aut(G)`, `Center(G)` circled over `Z(G)`, `Sign`, `Id`, the `Sign(σ) = n − r` slip.

### 11-10 (Week 9 Tuesday)
- Nearly all of `d076faf` is there: `φ` for the action, `x ∼̂_H y`, the `I ⊃ J ⊃ R` slip, `Ŝ`,
  `17 ∈ Num`, the red crosses through `≅`, `Rot(△)`, `r × v → r(v)`, double-hat faces,
  `σ_g · σ_{g⁻¹}`, `φ(γ, t) = γ(t)`, and the nine `TIMESTAMP-SUSPECT` comments.
- `⟹ impossible because of dim. theory` (L1338): `d076faf` had said "dim" was never written. The
  frame at 00:39:54 shows "⟹ IMPOSSIBLE because of dim theory", so **`HEAD` is right** here and the
  earlier review was wrong.
- Lost already in the 11-13 Hydrogen edition (`3947fad`), so they were in `f68edb4` too:
  - `H ⊂ G subgroup` and `N ⊂ G ← usually means normal` are now `H < G subgp`, `N < G` and
    `--- usually means normal` (L317, L321), and an aiNote (L337–340) tells the reader that "one
    chalkboard panel switches temporarily to H < G / N < G". The frame at 00:09:48 shows `H ⊂ G` and
    `N ⊂ G` with an arrow, as `d076faf` had. Note and aiNote are wrong. [Gemini, frame today]
  - `≅ A_5` is now `= A_5` (L766); the frame at 00:24:14 is from before he wrote it, so open.
  - `This is an injection ⇕ Ker(σ) = e` is now `⇓` (L2298); in the frame at 01:14:34 the arrowhead
    is clearly at the bottom, the top is unclear, so open.

### 11-11 (Week 9 Wednesday, no frame-checked baseline)
- `R ≇ C as rings (x² = −1)` (L270) and the aiNote (L296) are right: the frame at 00:09:14 shows
  `(X² = −1)`. `f68edb4` had `(x² + 1)` and an aiNote saying so, which was wrong. (Gemini claimed the
  opposite, calling the old note frame-verified; it never was.)
- Gemini lists three more note differences (`⟸` vs `⟺` at L610, `x_i` vs `x` at L1223/L1225);
  neither version was ever frame-checked, so they are open.

## C. Book conventions the rerun reversed (user decisions, not frame facts)

- **Subgroups in boxes: `\le` → `\subset`** (11-03: 18 → 4, 11-10: 14 → 1, with a new aiNote
  "Notation Convention: ⊂ for Subgroups", 11-03 L149). The book's rule (memory, 2026-11-06): the board
  writes ⊂ and the word "subgroup"; boxes keep `\le` because it is more exact. (Decided 2026-11-15:
  follow the lecturer, so the rerun's `⊂` stays, with `≤` as an aside; see G.)
- `Ord` → `ord` (see B); `Rot(Tetrahedron)`/`Rot(Cube)` → `Rot(Δ)`/`Rot(cube)`.
- "coset" is back in boxes that the reviews had kept to his words (11-03 L1525, L1551, L1569;
  11-04 L356, summary L1097); `4d7469b`/`2888d90` had moved cosets to aiNotes.
- `\faktor` for every quotient (style only).
- The same direction is now in the prompts, uncommitted: `prompt-engineering` has 12 modified files
  (not mine), and `last-refinement/last-refinement.md` there tells Stage 4 to remove `Ord`/`ord` and
  `Ker`/`ker` remarks "and standardize". Committed, that would make every future lecture drop the
  board's `Ord`.

## D. Figures

All 40 `tikzpicture`s of the six chapters (38 pages of the committed PDF) were rendered and looked
at on contact sheets; the S₇ cycle diagram, the cube with its diagonals and the two tetrahedron
rotations of 11-03 were zoomed. No label collisions, no wrong hidden edges, no placeholder drawings.
`3973234`'s problems (arcs through numbers, circle-and-polygon solids) did not come back. Board
details: the cube's diagonals are labelled `A–D` (board `a–d`, see B); the 11-10 tetrahedron keeps
the board's letters (D top, A left, B front, C right); the 11-03 round table has the five knights.

## E. Argon's audit claims, checked

- "Restored frame-verified board fixes (`4d7469b`)": true for the knights, the normality proof,
  `(1 3)(1 2)(1 3)` and both Ramanujan corrections; not for `Remember the ∼_N`, `bij`, the `Φ_mat`
  check, or the FIT slip (A1).
- "`C_z` vs `z` accurately distinguished": the board has `c_z`; this reverses `2888d90`.
- "(ii) Associativ. is literally on the board (00:47:20)": the note says `(ii) Associativity`;
  `d076faf` had `(ii) Associative`. Wording only, not settled.

## F. Gemini second opinion: what it saw

One read-only run per chapter, each given the complete `HEAD` file and the complete baseline file
(`f68edb4`, for 11-10 `d076faf`) and asked for math errors, lost math, and board notes that differ;
every run quoted the last line of the file as proof that it reached the end.

| Chapter | Model | Findings (math / lost / notes) | Kept here after checking |
|---|---|---|---|
| 10-27 | Gemini 3.8 Flash | 2 / 3 / 7 | `x^{\min}` (A9), `R^*` (B, frame), the board-note items; not the `\begin{remark}` point (layout only) |
| 10-28 | Gemini 3.8 Flash | 4 / 4 / 10 | A2–A5 and most notes; its "∃ h ∈ H" point is wrong (the frame agrees with `HEAD`) |
| 11-03 | Gemini 3.8 Flash | — | timed out at 25 min with no output; rerun with Hydrogen, see below |
| 11-04 | Gemini 3.8 Flash | 5 / 5 / 9 | A6, A7, A8, the notes; not the `\bigl(&` alignment point (it compiles, and a `\cdot` between cycles is not wrong) |
| 11-10 | Gemini 3.8 Flash | 0 / 0 / 5 | the `<`/`⊂` notes (frame), the two open ones |
| 11-11 | Gemini 3.8 Flash | 2 / 2 / 4 | the "canonically" wording; its `x² + 1` claim is wrong (frame) |

It did not see the frames, the review commit messages or the memory notes, so its board points
only compare two texts; each one used above was either confirmed by a frame or by the reviewed
text it cites.

11-03 (Week 8 Tuesday): rerun with Gemini 4 Hydrogen XHIGH in two halves (lines 1–1260 and
1200–2430), each with the complete baseline. Note that Hydrogen wrote this text. Both halves
quoted their last line. Findings (math / lost / notes): first half 4 / 4 / 9, second half 4 / 3 / 7.

- It found independently what A1 says (the `G` in the theorem box and in the normality proof), the
  lost `bij` and the lost `≝` in the `Φ_mat` check.
- New, checked and right: `prop:im-phi-hat` lost its hypothesis `n ≥ 2` (L612; `f68edb4` L609 had
  it); the basis vectors lost `^T` and gained a `v_3` that needs `n ≥ 3` (L313–317); the ℓ-cycle
  check no longer says that elements outside the cycle are fixed (L892–896); the circular-arrangement
  proposition writes the board's `k ⟶ k!/k` inside its formula (L975); "a (2+2)-cycle (A B)(C D)"
  (L1211) is not a cycle.
- Its point that `Rot(Δ) = A_4` should be `≅`: the box identifies rotations with vertex permutations
  just before (L1058), so `=` is fine under that identification; the theorem now says so explicitly.
- Note differences against the reviewed text, all taken: `·_1`, `·_2`; `f(x·y) = … ⟹ a·b ∈ Im(f)`;
  the `v_i` notes; `Φ_mat(σ̂σ)`; `{1, −1}`; `ē`-bar in `(ℤ/2ℤ, +, 0̄)`; no `k →`; no `⟹` before the
  two subgroup statements; `∈ N` (not `= n̂_1 ∈ N`); no `G` under `q(x)`; no added `⟺`/double arrow
  in the two definitions; `= (6 8 17)`.

## G. Restored on 2026-11-15

Everything in A and B was restored or fixed in the six chapters, plus the Hydrogen points above.
Conventions, after the user's decision to follow the lecturer ("you can use ≤ as an aside"):
`Ord`, lowercase `c_z`, his words in the boxes ("equivalence classes"; cosets in an aiNote aside) and
`Rot(Tetrahedron)`/`Rot(Cube)` in boxes were restored. `⊂` for subgroups in the boxes stays, as he
writes it, with `≤` named in an aiNote (Week 7 Wed, Week 8 Tue, Week 8 Wed, Week 9 Tue); the group
chapters already had no `≤` for subgroups left. The field stays `k` (his chalk K and k look the same).
Open items in B (`≅ A_5`, `⇕`) were set back to the frame-reviewed `d076faf` versions. Not changed:
the three places where `HEAD` was right, and Week 9 Wednesday's unreviewed notes.

Found while restoring, and restored as well:
- Week 7 Tuesday, two more frames (00:58:45, 01:04:50): the board has `(G_1, ·, e_1), (G_2, ·, e_2)`
  without subscripts (the rerun had added `·_1`, `·_2` and two notes pointing at them),
  `f ∘ g(i) = f(g(i))` (the rerun: `(1)`, `f(g(1))`) and `S_1 = {1 → 1}` (the rerun: `S_1 :`); the
  reviewed text had all three right.
- Week 7 Wednesday: `(ii) ⟨x⟩` (the rerun: `(2)`), and `φ: rotations → permutations of the long
  diagonals` (the rerun: `Rotation ↦ permutation of the diagonals`).
- Week 8 Wednesday: `Center(G)` joined to `ker(Conj)` by a vertical `=`.
- Week 8 Tuesday: the notation box keeps `x N` (he says "another convention is you just write xN"),
  without the word coset.
- Week 7 Tuesday: the boxes and headings number the two cases `Case (i)` / `Case (ii)`, as the board
  does (the speech line "Case (1)" is what he says and stays).

Gemini 4 Hydrogen XHIGH then read the complete applied diff in four parts (each quoted its last
`@@` line) and a follow-up delta. Taken from it: the Week 7 Tuesday exercise proof still had
`(x^{\min})` and now used `k` both as the field and as a summation index (fixed: `m`, index `j`);
Week 9 Tuesday's notation box still said `H < G`, `N < G` (now ⊂, with ≤ in the aiNote below), and a
box there wrote "Rotation group has order 60 = A_5" (now `|rotation group| = 60`, `≅ A_5`; this was
already in the 11-13 edition); leftover "coset" in Week 8 Tuesday's summary and conjugacy proof; the
aiNote title "Board Shorthand" (now "Board Slip"); `Rot(Octahedron)` and two PDF bookmark texts; a
`$C$` in Week 8 Wednesday's speech; one `\qt{you check}`. Not taken: `:=` in boxes (the book's rule
puts `:=` in boxes and the plain sign in notes), and three "unbalanced brace" / "Partitionsn" claims
that misread the word-diff format (the lines are balanced and the book compiles).
