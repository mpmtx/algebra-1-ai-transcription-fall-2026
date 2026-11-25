# Group Theory Content & Mathematical Review (Weeks 7–10, plus Early Group Sections)

**Date:** 2026-11-25 (revised per house-rule review)  
**Scope:**
- `content/prerequisites.tex` (Section 0.4, lines 191–216: *Groups, Fields and the Complex Numbers*)
- `content/step4-2026-09-22-tuesday-week2-algebra-1-offset-final.tex` (lines 126–825: *Review of Algebraic Structures*, *Group Homomorphisms and Isomorphisms*, *Kernels and Subgroups*)
- `content/step4-2026-10-27-tuesday-week7-algebra-1-offset-final.tex` (lines 922–2013: from `\section{Introduction to Groups}` to the end of the lecture)
- `content/step4-2026-10-28-wednesday-week7-algebra-1-offset-final.tex` (lines 1–1321)
- `content/step4-2026-11-03-tuesday-week8-algebra-1-offset-final.tex` (lines 1–2438)
- `content/step4-2026-11-04-wednesday-week8-algebra-1-offset-final.tex` (lines 1–1097)
- `content/step4-2026-11-10-tuesday-week9-algebra-1-offset-final.tex` (lines 1–2569)
- `content/step4-2026-11-11-wednesday-week9-algebra-1-offset-final.tex` (lines 1–1305)
- `content/step4-2026-11-17-tuesday-week10-algebra-1-offset-final.tex` (lines 1–2551)
- `content/step4-2026-11-18-wednesday-week10-algebra-1-offset-final.tex` (lines 1–1079)

---

## Executive Summary & House Conventions

1. **Overall Structural & Mathematical Health:**
   - All eight Week 7–10 lecture files pass `tools/rerun-check/timecheck.py` (`rc = 0`, monotonic timestamps, no inversions).
   - Every `\cref`, `\Cref`, `\eqref`, and `\ref` in the group theory chapters resolves cleanly with zero undefined or multiply-defined labels, and the compiled PDF (`algebra-1-transcription.pdf`, 755 pages) has zero `Overfull \hbox` warnings.
   - Major subtleties and slips are already handled cleanly in the lecture files—including $n \ge 2$ in `prop:im-phi-hat` and `prop:order-alternating-group`, Ramanujan's congruences ($7k+5, 11k+6$), $\operatorname{Sign}(\sigma) = n - r \mapsto (-1)^{n-r}$, right cosets of index-$2$ subgroups for infinite $G$, $D_{2n}$ for $n \ge 3$ vs.\ $n = 1, 2$, $\frac{1}{p} \notin \langle n/m \rangle$, Hamel-basis cardinality $\mathfrak{c} = 2^{\aleph_0}$, $x^2 = -1$ vs.\ spoken "$x^2 - 1$", Sylow II "divisible by" $\mapsto$ "that divide", and the beyond-the-lecture proof of Sylow IV.

2. **House Conventions Observed (`environments-inlinemetanote.md`, `speech-refinement.md`, `tools/rerun-check/README.md`):**
   - **Lecturer prose in `speech` is never rewritten.**
   - **`(i.e., ...)` in `speech`** is reserved strictly for audible word-slips ("says $a$ where context requires $x$"), never for informal phrasing or omitted hypotheses that are already stated accurately in the adjacent `content` box. When speech and board do not already confirm the word, a spoken slip requires checking the recording and adding `% [WORD-CHECKED: ...]` naming the witnesses (`tools/rerun-check/README.md`, step 5).
   - **Board formulas in `content`** are never replaced when the board is not marked as a slip; clarifications are added around the board formula (`environments-inlinemetanote.md`, "Every `writes` reappears in the next `content`").
   - **Board slips in `\inlinemetanote`** follow the prescribed form `writes \qt{...}, a slip for ...`.

---

## Summary Table of Active Findings

*(Original IDs `G1`–`G11` are preserved for cross-reference; `G4` and `G12` were dropped per house rules, and `G13`–`G14` cover two additional items.)*

| ID | Lecture | Lines | Location | Priority | Summary |
|---|---|---|---|---|---|
| **G1** | W2 Tue (`09-22`) | 733, 735 | `speech` | Holds | Neutral element of $(G, \cdot, e)$ spoken/written as $0$ (`0 \in H`, `(H, \cdot, 0)`) |
| **G2** | W7 Tue (`10-27`) | 945 | `content` (`def:group-w7tue`) | Holds | Tie `(G2)`'s $\exists\, e \in G$ back to the distinguished $e$ of $(G, \cdot, e)$ without replacing the board quantifier |
| **G3** | W7 Tue (`10-27`) | after 1695 | `content` (`steps`) | Minor | Add step-by-step cycle-tracing `steps` box for $(2\,3)(1\,3) = (1\,2\,3)$ matching lines 1661–1667 |
| **G13** | W7 Wed (`10-28`) | 910, 946–952 | `content` (TikZ) | Holds | Icosahedron front projection uses inner/outer radii `0.44 / 0.90` (ratio $2.05$) instead of golden-ratio projection $0.90 / \varphi \approx 0.56$ |
| **G5** | W7 Wed (`10-28`) | 1210 | `content` (beyond lecture) | Minor | Add one-sentence homomorphism check $(R_1 \circ R_2)(\ell) = R_1(R_2(\ell))$ at start of beyond-the-lecture proof |
| **G6** | W8 Tue (`11-03`) | 1071 | `\recap` | Holds | `\recap` cites `thm:tetrahedron-isomorphism` (and mentions Orbit–Stabilizer before Week 9) instead of `ex:tetrahedron-rotations-count` |
| **G14** | W8 Tue (`11-03`) | 2125 | `content` (`steps`) | Holds | `steps` box calls Jordan normal forms a "canonical complete set of representatives" right after noting non-uniqueness up to permuting blocks |
| **G7** | W8 Wed (`11-04`) | after 760 | `aiNote` | Optional | Optional one-line `aiNote` noting that the board/speech write $\faktor{\mathbb{Z}}{n\mathbb{Z}}$ without $n \ge 3$ (parallel to `prop:order-alternating-group`) |
| **G8** | W9 Tue (`11-10`) | 709; 844–845; 1181 | `content`, `insight`, `aiNote` | Holds | (1) `L709` "(and automorphism)" $\to$ "(and full symmetry)"; (2) add injectivity clause in `L844` `insight` + cycle-type `aiNote` for $5$ cubes in dodecahedron; (3) optional `\recap` to `def:pre-cyclic` at `L1181` |
| **G9** | W9 Wed (`11-11`) | 796 | `speech` | Holds (audio check) | `"$x$ times something"` $\to$ add `(i.e., $g \cdot x$ for some $g$)` at `L796` once confirmed in recording (`% [WORD-CHECKED: ...]`) |
| **G10** | W10 Tue (`11-17`) | 2160 (and 2205) | `content` | Minor | State `For $n \ge 2$,` on the $\operatorname{Stab}$ block characterization at `L2160` (and optionally `for $n \ge 2$` at `L2205` before `\eqref{eq:gln-recursion}`) |
| **G11** | W10 Wed (`11-18`) | after 1069 | `aiNote` | Minor | Short 3-line `aiNote` deriving the companion Sylow divisibility $n_p \mid m$ from transitivity of $G \curvearrowright S$ |

---

## Detailed Findings & Concrete Edits

### G1. Week 2 Tuesday (`content/step4-2026-09-22-tuesday-week2-algebra-1-offset-final.tex`, lines 733 & 735)
- **Context:** Throughout lines 131–730, the ambient group is $(G, \cdot, e)$ with multiplicative notation and neutral element $e$. At lines 733–735 (just before transitioning to rings and ideals), both speech and board switch to $0$ for the neutral element while keeping $\cdot$ for the product (`if $0 \in H$`, `$(H, \cdot, 0)$ is group`).
- **Fix (`speech` lines 733 & 735; speech and board agree on `0`, so no audio word-check is needed):**
  - Line 733: `if zero is in $H$ (i.e., $e$ is in $H$) \inlinemetanote{writes \qt{if $0 \in H$}}`
  - Line 735: `then this is a group (i.e., $(H, \cdot, e)$): \inlinemetanote{writes: $(H, \cdot, 0)$ is group}.`

---

### G2. Week 7 Tuesday (`content/step4-2026-10-27-tuesday-week7-algebra-1-offset-final.tex`, line 945)
- **Context:** `def:group-w7tue` (lines 941–948) introduces a tuple $(G, \cdot, e)$ with neutral element $e \in G$, and `(G2)` reproduces the board's `\exists\, e \text{ s.t. } ex = xe = x \;\; \forall x \in G`.
- **Issue:** Without tying the existentially quantified $e$ in `(G2)` back to the third entry of $(G, \cdot, e)$, $e$ in `(G2)` reads as a fresh bound variable rather than constraining the tuple's distinguished element.
- **Fix (`content` line 945, adding around the board formula without replacing it; no `aiNote` needed):**
  ```latex
      \item \textbf{(G2) Unit property:} $\exists\, e \in G$ such that $ex = xe = x \quad \forall x \in G$ (this is the $e$ of $(G, \cdot, e)$; it is unique, \cref{prop:group-unit-unique}).
  ```

---

### G3. Week 7 Tuesday (`content/step4-2026-10-27-tuesday-week7-algebra-1-offset-final.tex`, after line 1695)
- **Context:** In `speech` line 1683, when computing $(2\,3)(1\,3) = (1\,2\,3)$, the transition from obtaining $2 \mapsto 3$ to tracing the next input $3 \mapsto 1$ happens mid-sentence. Unlike $(1\,3)(2\,3) = (1\,3\,2)$ right above (lines 1661–1667), `content` lines 1688–1696 has no step-by-step trace box.
- **Fix (leave `speech` line 1683 untouched; add `steps` inside `content` after `obs:s3-non-commutative` at line 1695):**
  ```latex
  \begin{steps}[Step-by-Step Cycle Tracing]
  \begin{itemize}
      \item Starting at $1$: $(1\,3)$ sends $1 \mapsto 3$, and $(2\,3)$ sends $3 \mapsto 2$, so $1 \mapsto 2$.
      \item Continuing from $2$: $(1\,3)$ fixes $2$, and $(2\,3)$ sends $2 \mapsto 3$, so $2 \mapsto 3$.
      \item Continuing from $3$: $(1\,3)$ sends $3 \mapsto 1$, and $(2\,3)$ fixes $1$, closing $(1\,2\,3)$.
  \end{itemize}
  \end{steps}
  ```

---

### G13. Week 7 Wednesday (`content/step4-2026-10-28-wednesday-week7-algebra-1-offset-final.tex`, lines 910 & 946–952)
- **Context:** In the TikZ figure of the five Platonic solids, the dodecahedron (line 908) uses exact orthographic projection down a $5$-fold face axis (`r_2 = 0.92`, `r_1 = r_2 / phi = 0.92 / 1.618 = 0.57`), whereas the icosahedron (lines 910 & 946–952) uses `r_in = 0.44` and `r_out = 0.90`.
- **Issue:** In an orthographic projection of a regular icosahedron down a $3$-fold face axis (for instance, projecting the vertices $(0, \pm 1, \pm \varphi)$, $(\pm 1, \pm \varphi, 0)$, $(\pm \varphi, 0, \pm 1)$ perpendicular to $(1, 1, 1)$), the inner triangle has projected radius $\frac{2}{\sqrt{3}}$ and the outer regular hexagon has projected radius $\frac{2\varphi}{\sqrt{3}}$, so $\frac{r_{\text{out}}}{r_{\text{in}}} = \varphi = \frac{1+\sqrt{5}}{2} \approx 1.618$. Using `0.44` with `0.90` gives ratio $2.05$ instead of $\varphi$, making the central triangle noticeably too small.
- **Fix (`content` lines 910, 946, 950–952):** Change `0.44` to `0.56` ($= 0.90 / \varphi$, rounded to two decimals like `0.57` in the dodecahedron), and update the comment on line 910 accordingly (`inner triangle r_1 = r_2 / phi = 0.90 / 1.618 = 0.56`).

---

### G5. Week 7 Wednesday (`content/step4-2026-10-28-wednesday-week7-algebra-1-offset-final.tex`, line 1210)
- **Context:** The beyond-the-lecture proof in lines 1209–1221 proves injectivity of $\phi \colon \operatorname{Rot}(\text{Cube}) \to S_4$.
- **Fix (`content` line 1210):** Add one short sentence noting the homomorphism property: since $(R_1 \circ R_2)(\ell) = R_1(R_2(\ell))$ for each long diagonal line $\ell$, $\phi(R_1 \circ R_2) = \phi(R_1) \circ \phi(R_2)$.

---

### G6. Week 8 Tuesday (`content/step4-2026-11-03-tuesday-week8-algebra-1-offset-final.tex`, line 1071)
- **Context:**
  ```latex
  \recap{Compare \cref{thm:tetrahedron-isomorphism}, where $|\operatorname{Rot}(\text{Tetrahedron})| = 12$ was first computed via the orbit--stabilizer / counting argument.}
  ```
- **Issue:** `\cref{thm:tetrahedron-isomorphism}` only previewed $\operatorname{Rot}(\text{Tetrahedron}) \cong A_4$, whereas the $3 \cdot 4 = 12$ count is `\cref{ex:tetrahedron-rotations-count}`—and the Orbit–Stabilizer Theorem has not yet been introduced in Week 8 (it arrives in Week 9).
- **Fix (line 1071):**
  ```latex
  \recap{The count $|\operatorname{Rot}(\text{Tetrahedron})| = 12$ is \cref{ex:tetrahedron-rotations-count}.}
  ```
  *(Note: In `thm:rot-tetrahedron-a4` at line 1065, the clause "viewed inside $S_4$ through the permutations of the vertices" already covers identifying $\{A, B, C, D\}$ with $\{1, 2, 3, 4\}$.)*

---

### G14. Week 8 Tuesday (`content/step4-2026-11-03-tuesday-week8-algebra-1-offset-final.tex`, line 2125)
- **Context:** In `steps` (`[Indexing by Jordan Normal Form]`, line 2125):
  ```latex
  Going beyond the lecture: every invertible complex $n \times n$ matrix $A$ is conjugate in $\operatorname{GL}_n(\mathbb{C})$ to a Jordan normal form (with non-zero eigenvalues on the diagonal), and this Jordan normal form is unique up to permuting the Jordan blocks. Thus, Jordan normal forms provide a canonical complete set of representatives for the conjugacy classes of $\operatorname{GL}_n(\mathbb{C})$.
  ```
- **Issue:** Because permuting distinct Jordan blocks yields distinct Jordan matrices in the *same* conjugacy class (e.g., $\operatorname{diag}(1, 2)$ and $\operatorname{diag}(2, 1)$), raw Jordan normal forms do **not** form an irredundant canonical set of representatives—they classify conjugacy classes **up to permutation of the Jordan blocks** (equivalently, conjugacy classes are indexed by multisets of Jordan blocks with non-zero eigenvalues).
- **Fix (`content` line 2125):** Replace the final sentence with:
  ```latex
  Thus, Jordan normal forms modulo permutation of their Jordan blocks (equivalently, multisets of Jordan blocks with non-zero eigenvalues) index the conjugacy classes of $\operatorname{GL}_n(\mathbb{C})$.
  ```

---

### G7. Week 8 Wednesday (`content/step4-2026-11-04-wednesday-week8-algebra-1-offset-final.tex`, after line 760)
- **Context:** On the board and in `speech` line 734, $x \mapsto -x$ on $\faktor{\mathbb{Z}}{n\mathbb{Z}}$ is stated without $n \ge 3$; `ex:znz-negation` (line 751) supplies `($n \ge 3$)` and line 759 treats $n = 1, 2$.
- **Fix (optional, no anchor in `speech`):** At most one `aiNote` line noting that the board writes $\faktor{\mathbb{Z}}{n\mathbb{Z}}$ without the condition $n \ge 3$ (parallel to the `aiNote` for `prop:order-alternating-group` at line 431).

---

### G8. Week 9 Tuesday (`content/step4-2026-11-10-tuesday-week9-algebra-1-offset-final.tex`)
1. **Duality and symmetry groups (`content` line 709 only; leave `speech` line 654 untouched):**
   - Change `their rotation (and automorphism) groups coincide` in `content` line 709 to `their rotation (and full symmetry) groups coincide` so it is not conflated with $\operatorname{Aut}(\operatorname{Rot}(P))$.

2. **Faithfulness in the $5$-cubes isomorphism $\operatorname{Rot}(\text{Dodecahedron}) \cong A_5$ (`insight` line 844 + `aiNote` after line 845):**
   - In `insight` line 844, add injectivity/faithfulness:
     ```latex
     Each non-trivial rotation permutes these $5$ cubes non-trivially and as an even permutation, giving an injective homomorphism into $A_5 \subset S_5$ and hence (since $|\operatorname{Rot}(\text{Dodecahedron})| = 60 = |A_5|$) an isomorphism with $A_5$.
     ```
   - Place the explicit cycle-type check (which goes beyond the lecture) in an `aiNote` right after `insight` (line 845):
     ```latex
     \begin{aiNote}[Beyond the Lecture: Cycle Types on the Five Inscribed Cubes]
     Permuting the $5$ inscribed cubes defines a homomorphism $\psi \colon \operatorname{Rot}(\text{Dodecahedron}) \to S_5$. The $59$ non-identity rotations consist of $24$ face-axis rotations of order $5$ ($5$-cycles), $20$ vertex-axis rotations of order $3$ (fixing $2$ cubes, cycle type $3+1+1$), and $15$ edge-midpoint rotations of order $2$ (fixing $1$ cube and swapping the other $4$ in two pairs, cycle type $2+2+1$). Since none fixes all $5$ cubes and all have even cycle types, $\psi$ is injective with image in $A_5$.
     \end{aiNote}
     ```

3. **Infinite cyclic subgroup link (`content` line 1181, minor):**
   - Add a one-line `\recap` before `q:qstar-iso-z` pointing to `\cref{def:pre-cyclic}` for $\langle g \rangle$ in general (possibly infinite) groups (no new definition needed, as the proofs spell out the integer powers/multiples).

---

### G9. Week 9 Wednesday (`content/step4-2026-11-11-wednesday-week9-algebra-1-offset-final.tex`, line 796)
- **Context:** Proposing $C\bigl(g \cdot \operatorname{Stab}(x)\bigr) = g \cdot x$ for a left action $G \curvearrowright T$, line 796 says:
  ```latex
  It should be an element of the orbit, so it should be $x$ times something --- because that's what an element of the orbit is --- and $x$ times what?
  ```
- **Fix (`speech` line 796 only; leave line 812 untouched as `\inlinemetanote{writes: $g \cdot x$}` is already in that paragraph):**
  - Confirm `"$x$ times something"` against the audio recording; if confirmed, add a `% [WORD-CHECKED: ...]` comment above the `speech` block and insert `(i.e., $g \cdot x$ for some $g$)` after `$x$ times something` at line 796.

---

### G10. Week 10 Tuesday (`content/step4-2026-11-17-tuesday-week10-algebra-1-offset-final.tex`, line 2160 & line 2205)
- **Context:** Equation `\eqref{eq:stab-block-matrix}` (line 2162) writes $\operatorname{Stab}\bigl((1, 0, \dots, 0)^T\bigr)$ with a lower-right block in $\mathrm{GL}_{n-1}(\mathbb{F}_p)$, and `\eqref{eq:gln-recursion}` (line 2207, in the next `content` box right above the $n = 1$ base case) writes the recurrence in terms of $|\mathrm{GL}_{n-1}(\mathbb{F}_p)|$.
- **Fix (`content` line 2160, and optionally line 2205; no remark on $\mathrm{GL}_0$):**
  - Begin line 2160 with `For $n \ge 2$, an $n \times n$ matrix $A \in \mathrm{GL}_n(\mathbb{F}_p)$ fixes ...` (and optionally add `for $n \ge 2$` on line 2205 so `\eqref{eq:gln-recursion}` is self-contained next to the $n = 1$ base case).

---

### G11. Week 10 Wednesday (`content/step4-2026-11-18-wednesday-week10-algebra-1-offset-final.tex`, after line 1069)
- **Context:** The beyond-the-lecture proof of Sylow IV (lines 1049–1068) already explains why $G$ acts on $S$ by conjugation and restricts the action to $P \curvearrowright S$ to obtain $|S| \equiv 1 \pmod p$. Applying Orbit–Stabilizer to the full transitive action $G \curvearrowright S$ (from Sylow III) gives the companion divisibility constraint used alongside Sylow IV in textbooks.
- **Fix (concise 3-line `aiNote` after `content` line 1069):**
  ```latex
  \begin{aiNote}[Beyond the Lecture: Divisibility $|S| \mid m$]
  By Sylow~III (\cref{thm:sylow-3}), the conjugation action $G \curvearrowright S$ has a single orbit $S = \operatorname{Orb}_G(P)$ with stabilizer $N_G(P) \supset P$. Since $p^k = |P|$ divides $|N_G(P)|$, the Orbit--Stabilizer Theorem gives $|S| = \frac{|G|}{|N_G(P)|} = \frac{p^k m}{|N_G(P)|} \mid m$; thus the number $n_p := |S|$ of $p$-Sylow subgroups satisfies both $n_p \equiv 1 \pmod p$ and $n_p \mid m$.
  \end{aiNote}
  ```
