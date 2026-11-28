# Week 11 Follow-Up Review: Missing Steps, Precision, and Layout

**Date:** 2026-11-28 (follow-up to [week11-math-review.md](file:///C:/Users/miche/latex/algebra-1-ai-transcription-fall-2026/findings/week11-math-review.md) after commit `e1ffd3d` and the textbook's `findings/12` triage)  
**Scope:**
- **Week 11 Tue:** [step4-2026-11-24-tuesday-week11-algebra-1-offset-final.tex](file:///C:/Users/miche/latex/algebra-1-ai-transcription-fall-2026/content/step4-2026-11-24-tuesday-week11-algebra-1-offset-final.tex) (lines 1--1903)
- **Week 11 Wed:** [step4-2026-11-25-wednesday-week11-algebra-1-offset-final.tex](file:///C:/Users/miche/latex/algebra-1-ai-transcription-fall-2026/content/step4-2026-11-25-wednesday-week11-algebra-1-offset-final.tex) (lines 1--1182)
- Rendered pages 746--817 of [algebra-1-transcription.pdf](file:///C:/Users/miche/latex/algebra-1-ai-transcription-fall-2026/algebra-1-transcription.pdf)

---

## Executive Summary

Both Week 11 lectures pass `tools/rerun-check/timecheck.py`, all cross-references resolve, and all 13 TikZ figures across Tuesday and Wednesday render cleanly without collisions. However, cross-checking the lecture notes against the textbook's Week 11 review (`findings/12`, keeping only items that hold under the lecture-notes house rules: `speech` untouched, board formulas preserved, omitted derivations placed in `steps` or `[Beyond the Lecture]` `aiNote` boxes) plus inspecting the Week 11 build log and rendered PDF pages turned up:

1. **One `42.50pt` `Overfull \hbox`** on the classical Lie groups table (`W11 Tue` lines 926--936, printed p. 769)---the **only** `Overfull \hbox` in the entire 817-page transcription build.
2. **One missing theorem-hypothesis check** in the angle-trisection proof (`W11 Wed` line 1107: invoking `prop:tower-law` on $\mathbb{Q} \subset K \subset F_k$ without first noting $\dim_K F_k < \infty$).
3. **Three precision/terminology items** (connectedness of $\operatorname{GL}_n(\mathbb{R})$ and $\operatorname{O}_n$ in `W11 Tue` Section 11.5.3; defining *monic*; and noting $\beta$-dependence in `W11 Tue`'s Kronecker `aiNote`). *(Note: the working tree of `W11 Tue` already adds the non-degeneracy sentence for symplectic forms at line 937 and the word `simple` for the five exceptional Lie groups at line 959.)*
4. **Six "pen-and-paper" / self-sufficiency improvements** where the lecture notes currently assert non-trivial steps without justification (notably the $S_5$ counts and $A_5$ splitting in `W11 Tue` L589--591, the $|G| = pq$ classification at `W11 Tue` L788, and invoking the unproved Rational Root Theorem at `W11 Wed` L1166).

---

## Summary Table

| ID | Lecture | Lines | Target | Category | Summary |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **W11F-1** | W11 Tue | `926--936` | `content` (`tabular`) | Layout | Fix `42.50pt` `Overfull \hbox` on classical Lie groups table (only overfull box in the 817-page PDF) |
| **W11F-2** | W11 Wed | `1107` | `content` | Math rigor | Justify Hypothesis (1) of `prop:tower-law` ($\dim_K F_k < \infty$) before applying the Tower Law to $\mathbb{Q} \subset K \subset F_k$ |
| **W11F-3** | W11 Tue | after `938` | `aiNote` | Math precision | Note that $\operatorname{GL}_n(\mathbb{R})$ and $\operatorname{O}_n$ have two connected components (while $\operatorname{SL}_n(\mathbb{R}), \operatorname{SO}_n, \operatorname{U}_n, \operatorname{SU}_n, \operatorname{Sp}_{2n}$ are connected; Lorentz $\operatorname{O}(1,3)$) |
| **W11F-4** | W11 Tue (and W5 Wed) | Tue `1141`; W5 Wed `681` | `content` | Terminology | Define *monic* (leading coefficient $1$) after `def:poly-degree` in W5 Wed and add `(leading coefficient $1$)` at W11 Tue L1141 |
| **W11F-5** | W11 Tue | `1880--1884` | `aiNote` | Math precision | Note that $\bar{\phi} \colon K \xrightarrow{\sim} k(\beta)$ is canonical relative to the chosen root $\beta$ (e.g., $i$ vs.\ $-i$ in $\mathbb{C}$) |
| **W11F-6** | W11 Tue | `589--591` | `steps` | Missing steps | Prove the $S_5$ class counts ($1, 15, 20, 24$) and why $15, 20$ stay single classes in $A_5$ while $24$ splits into $12 + 12$ |
| **W11F-7** | W11 Tue | `511--513` | `steps` | Missing steps | Explain why $\{1,2,3,4\}$ gives $3$ double transpositions and why they form a single conjugacy class in $A_4$ |
| **W11F-8** | W11 Tue | after `789` | `aiNote` | Missing steps | Add `[Beyond the Lecture]` `aiNote` showing why $G = AB$ and how $\operatorname{Conj}_x(y) = y^a$ ($a^q \equiv 1 \pmod p$) classifies $|G| = pq$ |
| **W11F-9** | W11 Wed | `990, 1042--1045` | `content`, `steps` | Missing steps | Note `(one may take $E = \mathbb{Q}(\alpha)$)`, mention the quadratic formula/discriminant $d$, and warn that $\dim_{\mathbb{Q}} \mathbb{Q}(\alpha) = 2^m$ is not sufficient |
| **W11F-10** | W11 Wed | `1058--1062, 1096, 1166` | `content`, `steps` | Missing steps | Parentheticals for $60^\circ$ & perpendicular, 2-line derivation of $\cos(3\theta)$ via `fact:pre-complex`, and Euclid's-lemma proof replacing unproved "Rational Root Theorem" |
| **W11F-11** | W11 Tue & Wed | Tue `350, 1092, 1231, 1393, 1607`; Wed `322` | `content`, `steps`, `insight` | Quick bridges | Five one-clause justifications and `\cref` links removing small local jumps |

---

## 1. Layout & Build Hygiene

### W11F-1. `42.50pt` `Overfull \hbox` on the Classical Lie Groups Table (`W11 Tue`)
- **Location:** [step4-2026-11-24-tuesday-week11-algebra-1-offset-final.tex](file:///C:/Users/miche/latex/algebra-1-ai-transcription-fall-2026/content/step4-2026-11-24-tuesday-week11-algebra-1-offset-final.tex#L925-L936) (printed p. 769)
- **Issue:** Compilation reports `Overfull \hbox (42.49738pt too wide) in paragraph at lines 926--936`---the sole overfull box in the entire transcription PDF---because the three-column `tabular` sits inside a `content` box (narrower than `\textwidth` by its left rule and padding) with wide headers `\textbf{Classical Lie Groups}` and `\textbf{Physics Connection}`.
- **Suggested fix:** Use `@{}l l l@{}` and shorten the headers to `\textbf{Classical groups}` and `\textbf{Physics}` (matching textbook `ch16` L206), which trims ~85pt and clears the `content` box width with room to spare.

---

## 2. Mathematical Rigor, Precision, and Terminology

### W11F-2. Missing finite-dimensionality check $\dim_K F_k < \infty$ in Angle Trisection (`W11 Wed`)
- **Location:** [step4-2026-11-25-wednesday-week11-algebra-1-offset-final.tex](file:///C:/Users/miche/latex/algebra-1-ai-transcription-fall-2026/content/step4-2026-11-25-wednesday-week11-algebra-1-offset-final.tex#L1107-L1110)
- **Issue:** `prop:tower-law` ([W11 Wed L638--L648](file:///C:/Users/miche/latex/algebra-1-ai-transcription-fall-2026/content/step4-2026-11-25-wednesday-week11-algebra-1-offset-final.tex#L638-L648)) requires as Hypothesis **(1)** that the top field is finite-dimensional over the middle field. At line 1107, `W11 Wed` writes:
  > *"Now consider the tower $\mathbb{Q} \subset K \subset F_k$. By the Tower Law (`\cref{prop:tower-law}`): $\dim_{\mathbb{Q}} F_k = \dim_K F_k \cdot \dim_{\mathbb{Q}} K = \dim_K F_k \cdot 3$..."*

  without checking that $F_k$ is finite-dimensional over $K$ (unlike textbook `ch17` L533, which supplies this step).
- **Suggested fix:** Insert one sentence at line 1107 before invoking `prop:tower-law`: *"Note that $F_k$ is finite-dimensional over $K$, since any $\mathbb{Q}$-basis of $F_k$ spans $F_k$ over $K$ as well (`\cref{fact:pre-basis}`)."*

### W11F-3. Connectedness of $\operatorname{GL}_n(\mathbb{R})$ and $\operatorname{O}_n$ in Section 11.5.3 (`W11 Tue`)
- **Location:** [step4-2026-11-24-tuesday-week11-algebra-1-offset-final.tex](file:///C:/Users/miche/latex/algebra-1-ai-transcription-fall-2026/content/step4-2026-11-24-tuesday-week11-algebra-1-offset-final.tex#L877-L938)
- **Issue:** *(The working tree already adds non-degeneracy of symplectic forms at line 937 and `simple` before `Lie groups` at line 959.)* At speech line 877, right after listing $\operatorname{GL}_n(\mathbb{R})$, $\operatorname{SL}_n(\mathbb{R})$, $\operatorname{O}_n$, $\operatorname{SO}_n$, $\operatorname{U}_n$, $\operatorname{SU}_n$, and $\operatorname{Sp}_{2n}$, the lecturer says: *"So, these are the standard families of infinite connected groups..."* In fact, $\operatorname{GL}_n(\mathbb{R})$ ($\det > 0$ vs.\ $\det < 0$) and $\operatorname{O}_n$ ($\det = +1$ vs.\ $\det = -1$) each have two connected components.
- **Suggested fix:** Leave `speech` untouched and add a short `aiNote` (`[Beyond the Lecture: Connectedness and Relativity]`, `% [PERSISTENT, ADDITION]`) after line 938 noting that $\operatorname{SL}_n(\mathbb{R})$, $\operatorname{SO}_n$, $\operatorname{U}_n$, $\operatorname{SU}_n$, and $\operatorname{Sp}_{2n}$ are connected, whereas $\operatorname{GL}_n(\mathbb{R})$ and $\operatorname{O}_n$ each have two connected components (and that special relativity more precisely uses the Lorentz group $\operatorname{O}(1, 3)$ of $x_0^2 - x_1^2 - x_2^2 - x_3^2$ on $\mathbb{R}^4$).

### W11F-4. Define *monic* (`W11 Tue` and `W5 Wed`)
- **Locations:** [step4-2026-11-24-tuesday-week11-algebra-1-offset-final.tex L1141](file:///C:/Users/miche/latex/algebra-1-ai-transcription-fall-2026/content/step4-2026-11-24-tuesday-week11-algebra-1-offset-final.tex#L1141) and [step4-2026-10-14-wednesday-week5-algebra-1-offset-final.tex L681](file:///C:/Users/miche/latex/algebra-1-ai-transcription-fall-2026/content/step4-2026-10-14-wednesday-week5-algebra-1-offset-final.tex#L681)
- **Issue:** *Monic* is written on the board and used in `W11 Tue` (`L1135, 1141, 1146, 1171`, as well as `W6 Tue` L801 and `W6 Wed` L229), but was never defined at `def:poly-degree` (`W5 Wed` L674).
- **Suggested fix:** Add a sentence of prose right after `def:poly-degree` (`W5 Wed` L681) defining a non-zero polynomial with leading coefficient $1$ as `\newterm{monic}`, and add `(leading coefficient $1$)` as a reminder at `W11 Tue` L1141. *(Side note spotted on the same `monic` grep line in [W6 Tue L801](file:///C:/Users/miche/latex/algebra-1-ai-transcription-fall-2026/content/step4-2026-10-20-tuesday-week6-algebra-1-offset-final.tex#L801): `Neil's parabola` $\to$ `Neile's parabola`, after William Neile.)*

### W11F-5. Dependence of the canonical isomorphism $\bar{\phi} \colon K \xrightarrow{\sim} k(\beta)$ on the chosen root $\beta$ (`W11 Tue`)
- **Location:** [step4-2026-11-24-tuesday-week11-algebra-1-offset-final.tex L1880--L1884](file:///C:/Users/miche/latex/algebra-1-ai-transcription-fall-2026/content/step4-2026-11-24-tuesday-week11-algebra-1-offset-final.tex#L1880-L1884) (`aiNote` `[Beyond the Lecture: Kronecker's Theorem and Polynomials in \beta]`)
- **Suggested fix:** Append one sentence to the existing `aiNote` noting that $\bar{\phi}$ is the *unique* ring homomorphism $K \to k(\beta)$ extending $\operatorname{Id}_k$ and sending $\alpha \mapsto \beta$; if $k(\beta)$ contains another root $\beta'$ of $f$ (such as $-i$ alongside $i$ in $\mathbb{C} = \mathbb{R}(i)$), choosing $\beta'$ yields a different $k$-isomorphism ($\alpha \mapsto -i$, complex conjugation).

---

## 3. Pen-and-Paper / Missing-Steps Audit (`steps` & `aiNote` Additions)

### W11F-6. Unproved $S_5$ counts and $A_5$ class-splitting in `[Origin of the Class Sizes from S_5]` (`W11 Tue`)
- **Location:** [step4-2026-11-24-tuesday-week11-algebra-1-offset-final.tex L589--L591](file:///C:/Users/miche/latex/algebra-1-ai-transcription-fall-2026/content/step4-2026-11-24-tuesday-week11-algebra-1-offset-final.tex#L589-L591)
- **Issue:** Currently the `steps` box states only:
  > *"Going beyond the lecture: the even permutations in $S_5$ have cycle types $(1)$, $(12)(34)$, $(123)$, and $(12345)$, of sizes $1$, $15$, $20$, and $24$ respectively. The $15$ double transpositions and $20$ $3$-cycles remain single conjugacy classes in $A_5$, whereas the $24$ $5$-cycles split into two $A_5$-conjugacy classes of size $12$ each."*

  Unlike the textbook (which proves both claims in `sol:a5-conjugacy-classes`), a reader of the lecture notes has to derive both the cycle counts and the $A_5$ splitting criterion from scratch on paper.
- **Suggested fix:** Expand this `steps` box by ~6 lines:
  - **Counts in $S_5$ (`\cref{prop:sign-from-cycles}`):** $5 \cdot 3 = 15$ (choose the fixed point, then pair the other four in $3$ ways), $\binom{5}{3} \cdot 2 = 20$ (choose three numbers and one of two cyclic orders), and $4! = 24$ (write a $5$-cycle starting with $1$).
  - **Splitting in $A_5$:** For $\sigma \in A_5$ with centralizer $C' \subset S_5$ and $C = C' \cap A_5$, Orbit--Stabilizer gives class sizes $120 / |C'|$ in $S_5$ and $60 / |C|$ in $A_5$. If $C'$ contains an odd permutation $\tau$, multiplication by $\tau$ bijects even and odd elements of $C'$ (`\cref{def:sign-homomorphism}`), so $|C| = |C'|/2$ and the class does not split: $(1\,2)(3\,4)$ commutes with odd $(1\,2)$, and $(1\,2\,3)$ commutes with odd $(4\,5)$. For any $5$-cycle $\sigma$, $|C'| = 120 / 24 = 5$, so $C' = \langle \sigma \rangle \subset A_5$, $|C| = 5$, and its $A_5$-class has $60 / 5 = 12$ elements; hence the $24$ $5$-cycles form two classes of $12$.

### W11F-7. Double-transposition count and single-class check in $A_4$ (`W11 Tue`)
- **Location:** [step4-2026-11-24-tuesday-week11-algebra-1-offset-final.tex L481, L511--L513](file:///C:/Users/miche/latex/algebra-1-ai-transcription-fall-2026/content/step4-2026-11-24-tuesday-week11-algebra-1-offset-final.tex#L511-L513)
- **Issue:** Speech line 481 says *"Three, because you can write this in three ways"* (spoken shorthand for partitioning $\{1,2,3,4\}$ into two pairs), and the `steps` box at lines 511--513 explains only why the $3$-cycles split, leaving the reader to check why the $3$ double transpositions form a single class in $A_4$.
- **Suggested fix:** Add two sentences at the start of the `steps` box at line 511 (e.g., titled `[Conjugacy Classes in $A_4$]`): $\{1, 2, 3, 4\}$ splits into two pairs in $3$ ways ($1$ paired with $2$, $3$, or $4$), and conjugating $(1\,2)(3\,4)$ by the even permutations $(1\,2\,3)$ and $(1\,3\,2)$ relabels it (`\cref{thm:conjugation-sn-formula}`) to $(2\,3)(1\,4)$ and $(3\,1)(2\,4)$, so all three lie in one $A_4$-class. (Also cite `\cref{rem:normal-conjugate-closed}` in the `steps` box at line 648.)

### W11F-8. How $\operatorname{Conj}_x$ classifies groups of order $pq$ (`W11 Tue`)
- **Location:** [step4-2026-11-24-tuesday-week11-algebra-1-offset-final.tex after L789](file:///C:/Users/miche/latex/algebra-1-ai-transcription-fall-2026/content/step4-2026-11-24-tuesday-week11-algebra-1-offset-final.tex#L784-L789)
- **Issue:** Line 788 concludes *"This map tells how the generators of $\faktor{\mathbb{Z}}{q\mathbb{Z}}$ and $\faktor{\mathbb{Z}}{p\mathbb{Z}}$ interact, and studying what it can be classifies all groups of order $pq$,"* without explaining why $A$ and $B$ generate all of $G$ or what $\operatorname{Conj}_x$ can be.
- **Suggested fix:** Add a concise `aiNote` (`[Beyond the Lecture: Classifying Groups of Order $pq$]`, `% [PERSISTENT, ADDITION]`) after line 789:
  1. By Lagrange, $|A \cap B|$ divides $p$ and $q$, so $A \cap B = \{e\}$; hence the $pq$ products $y b$ ($y \in A$, $b \in B$) are distinct and $G = A B$, with $(y_1 x^i)(y_2 x^j) = y_1 \operatorname{Conj}_x^i(y_2) x^{i+j}$.
  2. Fixing a generator $y_0$ of $A \cong \faktor{\mathbb{Z}}{p\mathbb{Z}}$, any automorphism $\operatorname{Conj}_x$ has the form $y \mapsto y^a$ ($1 \le a \le p - 1$). Since $\operatorname{Conj}_{x^q} = \operatorname{Conj}_e = \operatorname{Id}_A$, iterating $q$ times gives $a^q \equiv 1 \pmod p$, so the order of $\bar{a} \in (\faktor{\mathbb{Z}}{p\mathbb{Z}})^*$ divides both $q$ and $p - 1$.
  3. If $q \nmid p - 1$, then $a = 1$: $x$ commutes with $y_0$, $\operatorname{Ord}(y_0 x) = pq$, and $G = \langle y_0 x \rangle \cong \faktor{\mathbb{Z}}{pq\mathbb{Z}}$ (e.g., every group of order $15$ is cyclic); if $q \mid p - 1$, there is also one non-abelian group up to isomorphism ($D_{2p}$ when $q = 2$).

### W11F-9. Role of $E$, quadratic formula, and degree-$2^m$ warning in Constructible Numbers (`W11 Wed`)
- **Location:** [step4-2026-11-25-wednesday-week11-algebra-1-offset-final.tex L986--L1046](file:///C:/Users/miche/latex/algebra-1-ai-transcription-fall-2026/content/step4-2026-11-25-wednesday-week11-algebra-1-offset-final.tex#L986-L1046)
- **Suggested fixes:**
  1. At line 990, add `(one may take $E = \mathbb{Q}(\alpha)$)` so the role of the intermediate subfield $E$ from the board is clear.
  2. In `steps` `[Why Only Quadratic Extensions Arise]` (line 1042), add *"by the quadratic formula, with $d \in F_m$ its discriminant"*.
  3. At line 1045, add one sentence noting that while $\dim_{\mathbb{Q}} \mathbb{Q}(\alpha)$ divides $2^k$ by the Tower Law, having degree a power of $2$ is necessary but **not** sufficient for constructibility (an irreducible quartic over $\mathbb{Q}$ can have a real root of degree $4 = 2^2$ that lies in no tower of quadratic extensions).

### W11F-10. $60^\circ$ / $\cos(20^\circ)$ geometry, triple-angle formula, and self-contained Rational Root check (`W11 Wed`)
- **Locations:** [step4-2026-11-25-wednesday-week11-algebra-1-offset-final.tex L1058--L1062, L1094--L1096, L1165--L1172](file:///C:/Users/miche/latex/algebra-1-ai-transcription-fall-2026/content/step4-2026-11-25-wednesday-week11-algebra-1-offset-final.tex#L1058-L1172)
- **Issues & suggested fixes:**
  1. **Geometry (`L1058--L1062`):** Add brief parentheticals noting that an equilateral triangle is constructed by intersecting two circles of radius $1$ centered at $(0, 0)$ and $(1, 0)$, and that the perpendicular is dropped *"from the point at distance $1$ on the $20^\circ$ ray"*.
  2. **Triple-angle identity (`L1094--L1096`):** Add a 2-line `steps` box (or parenthetical citing `\cref{fact:pre-complex}`, where angles add under complex multiplication) deriving $\cos(3\theta) = \operatorname{Re}\bigl((\cos\theta + i\sin\theta)^3\bigr) = \cos^3\theta - 3\cos\theta(1 - \cos^2\theta) = 4\cos^3\theta - 3\cos\theta$.
  3. **Unproved "Rational Root Theorem" (`L1166`):** Line 1166 cites *"By the Rational Root Theorem"*, which has never been stated or proved anywhere in the lecture notes. Replace that citation with the 3-line self-contained proof (as in textbook `sol:cubic-irreducible`): if $f(p/q) = 0$ with $p, q \in \mathbb{Z}$, $q > 0$, and $(p, q) = 1$ ($p \neq 0$ since $f(0) = -1$), clearing denominators gives $8p^3 - 6pq^2 - q^3 = 0$; then $p \mid q^3$ forces $p = \pm 1$ by Euclid's lemma (`\cref{fact:pre-euclid}`), and $q \mid 8p^3 = \pm 8$ gives $q \in \{1, 2, 4, 8\}$.

### W11F-11. Quick One-Line Bridges (`W11 Tue` & `W11 Wed`)

| Location | Current jump | Minimal addition |
| :--- | :--- | :--- |
| [W11 Tue L350](file:///C:/Users/miche/latex/algebra-1-ai-transcription-fall-2026/content/step4-2026-11-24-tuesday-week11-algebra-1-offset-final.tex#L350) (`lem:q-in-normalizer`) | *"Since $Q$ is a subgroup of $G$, for every $x \in Q$ we have $x Q x^{-1} = Q$"* (closure alone gives $\subset$). | Add *(closure gives $x Q x^{-1} \subset Q$, and every $q \in Q$ equals $x (x^{-1} q x) x^{-1} \in x Q x^{-1}$)*. |
| [W11 Tue L1091--L1095](file:///C:/Users/miche/latex/algebra-1-ai-transcription-fall-2026/content/step4-2026-11-24-tuesday-week11-algebra-1-offset-final.tex#L1091-L1095) (`Reduction via Factorization`) | Uses $(g_1 \cdot g_2)(\alpha) = g_1(\alpha) \cdot g_2(\alpha)$ and absence of zero divisors without links. | Cite `(\cref{thm:universal-property-polynomial-ring}: evaluation at $\alpha$ is a ring homomorphism)` and `(\cref{ex:fields-are-domains})`. |
| [W11 Tue L1231](file:///C:/Users/miche/latex/algebra-1-ai-transcription-fall-2026/content/step4-2026-11-24-tuesday-week11-algebra-1-offset-final.tex#L1231) (`steps` degree $2$ or $3$) | Shows no roots $\implies$ irreducible in degrees $2, 3$ without showing why degree $4$ fails. | Add one sentence: *In degree $4$ this fails: $(x^2 + 1)^2$ has no root in $\mathbb{R}$ but is reducible over $\mathbb{R}$.* |
| [W11 Tue L1393](file:///C:/Users/miche/latex/algebra-1-ai-transcription-fall-2026/content/step4-2026-11-24-tuesday-week11-algebra-1-offset-final.tex#L1393) & [L1607](file:///C:/Users/miche/latex/algebra-1-ai-transcription-fall-2026/content/step4-2026-11-24-tuesday-week11-algebra-1-offset-final.tex#L1607) | Image of $k$ is a *subfield* (L1393); intersection of subfields is a *subfield* (L1607). | Add *(a subring by `\cref{prop:image-ring-hom-subring}`, with inverses $\bar{\gamma}^{-1} = \overline{\gamma^{-1}}$)* at L1393; add *($0$, $1$, sums, negatives, products, and inverses of non-zero elements lie in each $L$, hence in the intersection)* at L1607. |
| [W11 Wed L322](file:///C:/Users/miche/latex/algebra-1-ai-transcription-fall-2026/content/step4-2026-11-25-wednesday-week11-algebra-1-offset-final.tex#L322) (`insight` degree-$1$ case) | States $\dim_k K = 1$, i.e., $K \cong k$. | Add *($\bar{1}$ alone spans $K$ over $k$, so the canonical embedding $k \hookrightarrow K$ is surjective)*. |

---

## Resolution (2026-11-28)

Applied by Claude in the commit that adds this file, together with the textbook review's findings that carry over (book `findings/12`); speech untouched.

- **W11F-1:** already resolved: the overfull table came from an intermediate edit (the cell "(non-degenerate, skew-symmetric)"), which was reverted; the non-degeneracy now stands in a sentence under the table, and the headers stay.
- **W11F-2:** applied, one sentence before the Tower Law.
- **W11F-3:** applied as a `Spoken Slip` note (`% [PERSISTENT]`, the house form for a lecturer's slip), plus a separate `Beyond the Lecture: The Lorentz Group` note.
- **W11F-4:** applied; *monic* is defined in an addition note right after the W5 Wed content box (an addition does not go into the box), with the reminder in W11 Tue; Neil's parabola is now Neile's parabola (W6 Tue).
- **W11F-5, W11F-6, W11F-7** (including the cref at the Klein-group steps), **W11F-8:** applied.
- **W11F-9:** applied; "one may take E = Q(alpha)" and the power of 2 that is necessary but not sufficient form an addition note after the content box; the quadratic formula is in the steps box.
- **W11F-10:** applied; the triple-angle derivation is a `steps` box, and the Rational Root Theorem is replaced by the Euclid's-lemma argument (with p != 0).
- **W11F-11:** all five bridges applied.
- **From the textbook review:** "the simple Lie groups" in the box on the exceptional groups, and the statement of `thm:uniqueness-root-extension` without parentheses around "sending alpha to beta".
