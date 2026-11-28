# Week 11 Mathematical Review (Tuesday 2026-11-24 & Wednesday 2026-11-25)

**Date:** 2026-11-28 (revised after source & house-rule cross-check)  
**Scope:**
- **Week 11 Tue:** [step4-2026-11-24-tuesday-week11-algebra-1-offset-final.tex](file:///C:/Users/miche/latex/algebra-1-ai-transcription-fall-2026/content/step4-2026-11-24-tuesday-week11-algebra-1-offset-final.tex) (lines 1–1895: *Sylow's Fourth Theorem, Simple Groups, and Field Extensions*)
- **Week 11 Wed:** [step4-2026-11-25-wednesday-week11-algebra-1-offset-final.tex](file:///C:/Users/miche/latex/algebra-1-ai-transcription-fall-2026/content/step4-2026-11-25-wednesday-week11-algebra-1-offset-final.tex) (lines 1–1181: *Simple Field Extensions, the Tower Law, and Constructible Numbers*)

---

## Executive Summary

Overall, the mathematical content of both Week 11 lectures is in strong shape:
- All core proofs—Sylow IV via the normalizer $N(Q)$, non-existence of an order-$6$ subgroup in $A_4$ (including the explicit $3$-cycle splitting check in `steps`), simplicity of $A_5$ ($10$ proper sums checked), the beyond-the-lecture proofs for $|G| = p^2$ and $|G| = pq$, maximality of $(f) \subset k[x]$, Kronecker's construction $K = \faktor{k[x]}{(f)}$, uniqueness $K \cong k(\beta)$, $\dim_k K = \operatorname{degree}(f)$, the Tower Law, and the Rational Root Test check for $8x^3 - 6x - 1$—are logically sound and arithmetically verified, and all `\cref`/`\eqref` references resolve cleanly.
- Following the repository's house conventions, board formulas are never silently altered when not marked as slips/shorthand, and spoken prose is left unrewritten.

After cross-checking against the video frames, audio clips, and house conventions, there are **0 High / 0 Medium** issues and **8 Low-severity precision, convention, and notation items** *(original IDs preserved for cross-reference; `W11-M1`–`W11-M3` reclassified from Medium to Low as none alters the truth of a theorem, and `W11-L1` plus sub-items `W11-M3(1,3)` and `W11-L5(3)` dropped—see Section 2)*:

| ID | Lecture | Lines | Location | Severity | Summary |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **W11-M1** | W11 Tue & Wed | Tue `1164`; Wed `259, 265, 272` | `proof`, `content`, `steps` | Low | Add the $r = 0$ remainder case alongside $\deg(r) < d$ (`def:poly-degree` leaves $\deg(0)$ undefined) and remove $\operatorname{degree}(0) = -\infty$ at Wed `L272` (`rem:deg-zero-convention`) |
| **W11-M2** | W11 Tue | `821, 864–870, 926–928, 1891` | `speech`, `content` (table), `overview` | Low | Table cell $\mathbb{C} \to \mathbb{C}^n$ for $\operatorname{U}_n, \operatorname{SU}_n$ (keeping board's `$\mathbb{C}, \langle , \rangle$` marked as shorthand) and upright `\operatorname` for $\operatorname{O}_n, \operatorname{SO}_n, \operatorname{U}_n, \operatorname{SU}_n, \operatorname{Sp}_{2n}$ |
| **W11-M3** | W11 Wed | `1041` | `steps` | Low | Add `(with $a, b, r^2 \in F_m$)` in the Line $\cap$ Circle item (explaining why $(x-a)^2 + (y-b)^2 = r^2$ has coefficients in $F_m$ even when $r \notin F_m$) |
| **W11-L2** | W11 Tue | `347` | `lem:q-in-normalizer` | Low | Add `For a subgroup $Q \subset G$,` in standalone `lem:q-in-normalizer` (`def:normalizer` above only assumes a subset $Q \subset G$) |
| **W11-L3** | W11 Tue | `536, 574` | `aiNote`, `speech` | Low | Add one-sentence `aiNote` after `def:simple-group` noting the standard textbook exclusion $G \neq \{e\}$; change `(slip for $A_4$)` $\to$ `(i.e., $A_4$)` at `L574` |
| **W11-L4** | W11 Tue | `779`, `1086` (`1152` verified) | `content` | Low | Clarify that $\faktor{\mathbb{Z}}{p\mathbb{Z}}, \faktor{\mathbb{Z}}{q\mathbb{Z}}$ stand for $A, B \subset G$ written multiplicatively (`L779`), and specify `a non-zero $f$` (`L1086`); `$a$` at `L1152` confirmed verbatim in audio |
| **W11-L5** | W11 Tue | `1762, 1866, 1868` | `content` | Low | Write `$\bar{\phi} \colon K \xrightarrow{\sim} k(\beta)$ (the $\phi$ of \cref{thm:uniqueness-root-extension})` at `L1868` and `$\operatorname{Im}(\bar{\phi}) = \operatorname{Im}(\phi) = k(\beta)$` at `L1866`; cite `\cref{thm:universal-property-polynomial-ring}` at `L1762` |
| **W11-L6** | W11 Wed | `384, 443, 648, 877, 927, 1102, 1177` | `content`, TikZ | Low | `\id_k` $\to$ `\operatorname{Id}_k` (`L384, 1177`), note "degree of the extension" = $\dim_k E$ (`L648`), name Step 2 in distinctness parenthetical (`L877`), note $\phi|_{\mathbb{Q}} = \operatorname{Id}_{\mathbb{Q}}$ for $\mathbb{Q}$-dimensions (`L1102`), arrow start `1.15` $\to$ `1.35` (`L443/454–455`), and fix stale `hidden` plan line (`L927`) |

---

## 1. Active Findings (Low Severity)

### W11-M1. Undefined $\deg(0)$ vs.\ Polynomial Division Remainder Condition (Tue & Wed)

- **Locations:**
  - [step4-2026-11-24-tuesday-week11-algebra-1-offset-final.tex](file:///C:/Users/miche/latex/algebra-1-ai-transcription-fall-2026/content/step4-2026-11-24-tuesday-week11-algebra-1-offset-final.tex#L1163-L1167) (`proof` of `prop:root-linear-factor`, line 1164)
  - [step4-2026-11-25-wednesday-week11-algebra-1-offset-final.tex](file:///C:/Users/miche/latex/algebra-1-ai-transcription-fall-2026/content/step4-2026-11-25-wednesday-week11-algebra-1-offset-final.tex#L255-L274) (`Generation via the Division Algorithm` and `steps` in `prop:dim-quotient-field`, lines 257–273)
- **Issue:**
  In Week 5 Wednesday ([step4-2026-10-14-wednesday-week5-algebra-1-offset-final.tex](file:///C:/Users/miche/latex/algebra-1-ai-transcription-fall-2026/content/step4-2026-10-14-wednesday-week5-algebra-1-offset-final.tex#L676-L727), `def:poly-degree` and `rem:deg-zero-convention`), the course explicitly defines $\deg(0)$ to be **undefined** (`\deg(0) \longleftarrow \text{Undefined}`), relegates $\deg(0) = -\infty$ to a `[Beyond the Lecture]` `aiNote`, and states `thm:poly-long-division` with the dichotomy $r(x) = 0$ or $(r(x) \neq 0 \text{ and } \deg(r) < \deg(g))$.
  1. **Tuesday, line 1164:** In the proof of $f(\alpha) = 0 \iff (x - \alpha) \mid f$, line 1164 writes *"a remainder $r \in k[x]$ of degree less than $1$ (hence, a constant $r \in k$)"*, omitting the $r = 0$ alternative in the exact case $f(\alpha) = 0$.
  2. **Wednesday, lines 259, 265, 272:** Line 257 preserves the board's shorthand $\operatorname{degree}(r) < d$, while lines 259 and 265 omit the $r(x) = 0$ case of `thm:poly-long-division`, and `steps` line 272 invokes $\operatorname{degree}(0) = -\infty < d$, clashing with `rem:deg-zero-convention`.
- **Agreed Fix:**
  - **Tuesday line 1164:** `with $r = 0$ or $\deg(r) < 1$ (in either case a constant $r \in k$)`.
  - **Wednesday lines 259, 265, 272:** Keep the board's `degree(r) < d` in the display (`L257`) and board note (`L245`); supply the $r(x) = 0$ case of `\cref{thm:poly-long-division}` at `L259` and `L265`; and drop the $\operatorname{degree}(0) = -\infty$ parenthetical at `L272`.

---

### W11-M2. $\mathbb{C}^n$ for $\operatorname{U}_n, \operatorname{SU}_n$, and Upright `\operatorname` for Classical Lie Groups (Tue)

- **Location:** [step4-2026-11-24-tuesday-week11-algebra-1-offset-final.tex](file:///C:/Users/miche/latex/algebra-1-ai-transcription-fall-2026/content/step4-2026-11-24-tuesday-week11-algebra-1-offset-final.tex#L864-L931) (lines 864–870, 925–928) and [line 1891](file:///C:/Users/miche/latex/algebra-1-ai-transcription-fall-2026/content/step4-2026-11-24-tuesday-week11-algebra-1-offset-final.tex#L1891).
- **Issue:**
  1. Row 3 of the classical Lie groups table (line 927) writes `$\mathbb{C}, \langle \cdot, \cdot \rangle$ (Hermitian inner product)` from the board's shorthand `$\mathbb{C}, \langle , \rangle$` (frame `00:40:15`, where the lecturer says *"some complex thing and have a Hermitian inner product"*), whereas $\operatorname{U}_n, \operatorname{SU}_n$ act on $\mathbb{C}^n$ (parallel to $\mathbb{R}^n$ in rows 1–2).
  2. Multi-letter/classical Lie group names (`O_n, SO_n, U_n, SU_n, Sp_{2n}`) appear in math italics in the table (`L926–928`), summary (`L1891`), speech (`L866`), and board notes (`L866–870`), whereas `\operatorname{GL}` / `\operatorname{SL}` / `\operatorname{SO}` / `\operatorname{SU}` use `\operatorname` elsewhere in the book.
- **Agreed Fix:**
  - Change the table cell at `L927` from `\mathbb{C}` to `\mathbb{C}^n`, while keeping `\mathbb{C}, \langle , \rangle` in the board note at `L868` marked as shorthand.
  - Use upright `\operatorname{O}_n, \operatorname{SO}_n, \operatorname{U}_n, \operatorname{SU}_n, \operatorname{Sp}_{2n}` uniformly in the table, summary, speech, and notes (matching `\operatorname{GL}`, used 69 times across the book).

---

### W11-M3. Circle Equation Coefficient Clarification $r^2 \in F_m$ in `steps` (Wed)

- **Location:** [step4-2026-11-25-wednesday-week11-algebra-1-offset-final.tex](file:///C:/Users/miche/latex/algebra-1-ai-transcription-fall-2026/content/step4-2026-11-25-wednesday-week11-algebra-1-offset-final.tex#L1037-L1045) (`steps` line 1041).
- **Issue:** Setting a compass between two previously constructed points in $F_m^2$ can yield a radius $r \notin F_m$ (e.g., $\sqrt{2}$ over $\mathbb{Q}$), whereas $r^2 \in F_m$ always holds and is all the circle equation $(x - a)^2 + (y - b)^2 = r^2$ uses.
- **Agreed Fix:** Add `(with $a, b, r^2 \in F_m$)` in the **Line $\cap$ Circle** item on line 1041.

---

### W11-L2. Subgroup Hypothesis in Standalone `lem:q-in-normalizer` (Tue)

- **Location:** [step4-2026-11-24-tuesday-week11-algebra-1-offset-final.tex](file:///C:/Users/miche/latex/algebra-1-ai-transcription-fall-2026/content/step4-2026-11-24-tuesday-week11-algebra-1-offset-final.tex#L320-L352) (line 347).
- **Issue:** `def:normalizer` (line 321) only assumes a subset $Q \subset G$, whereas `lem:q-in-normalizer` (line 347) requires $Q$ to be a subgroup (as spoken at line 333: *"because $Q$ is a subgroup"*).
- **Agreed Fix:** Begin `lem:q-in-normalizer` (line 347) with `For a subgroup $Q \subset G$, ...`

---

### W11-L3. Trivial Group Convention Note after `def:simple-group` and Slip Tag on Line 574 (Tue)

- **Location:** [step4-2026-11-24-tuesday-week11-algebra-1-offset-final.tex](file:///C:/Users/miche/latex/algebra-1-ai-transcription-fall-2026/content/step4-2026-11-24-tuesday-week11-algebra-1-offset-final.tex#L533-L536) (`def:simple-group`) and [line 574](file:///C:/Users/miche/latex/algebra-1-ai-transcription-fall-2026/content/step4-2026-11-24-tuesday-week11-algebra-1-offset-final.tex#L574).
- **Agreed Fix:**
  1. Leave `def:simple-group` untouched and add a one-sentence `aiNote` (`[Beyond the Lecture]`, `% [PERSISTENT, ADDITION]`) after line 536 noting that textbooks also require $G \neq \{e\}$.
  2. Change `(slip for $A_4$)` to house form `(i.e., $A_4$)` on speech line 574.

---

### W11-L4. Multiplicative Identification of $\faktor{\mathbb{Z}}{p\mathbb{Z}}, \faktor{\mathbb{Z}}{q\mathbb{Z}} \subset G$ and Non-Zero $f$ Guard (Tue)

- **Locations in [step4-2026-11-24-tuesday-week11-algebra-1-offset-final.tex](file:///C:/Users/miche/latex/algebra-1-ai-transcription-fall-2026/content/step4-2026-11-24-tuesday-week11-algebra-1-offset-final.tex):**
  1. **[Line 779](file:///C:/Users/miche/latex/algebra-1-ai-transcription-fall-2026/content/step4-2026-11-24-tuesday-week11-algebra-1-offset-final.tex#L779-L782):** Add a short parenthetical noting that $\faktor{\mathbb{Z}}{p\mathbb{Z}}, \faktor{\mathbb{Z}}{q\mathbb{Z}}$ stand for $A, B \subset G$, written with $G$'s multiplication.
  2. **[Line 1086](file:///C:/Users/miche/latex/algebra-1-ai-transcription-fall-2026/content/step4-2026-11-24-tuesday-week11-algebra-1-offset-final.tex#L1086-L1090):** Specify `a non-zero $f$` before *"strictly lower degree"* on line 1090 (excluding $0 = 0 \cdot x$ before irreducibility is introduced on line 1114).
  3. **[Line 1152](file:///C:/Users/miche/latex/algebra-1-ai-transcription-fall-2026/content/step4-2026-11-24-tuesday-week11-algebra-1-offset-final.tex#L1152) *(audio-checked — no text change needed)*:** Checked via Gemini Neon on `00:55:35–00:56:35`: the lecturer says `"alpha"` in the first sentence (`L1148`) and `"f of a"`, `"x minus a"` in the second (`L1152`), so `$a$` in `speech` stays verbatim while the board note keeps `$\alpha$` *(optional: record this in a `% [WORD-CHECKED: ...]` comment above `L1147`)*.

---

### W11-L5. Avoiding Overloaded $\phi$ in the Proof of `thm:uniqueness-root-extension` and Adding `\cref` (Tue)

- **Locations in [step4-2026-11-24-tuesday-week11-algebra-1-offset-final.tex](file:///C:/Users/miche/latex/algebra-1-ai-transcription-fall-2026/content/step4-2026-11-24-tuesday-week11-algebra-1-offset-final.tex):**
  1. **[Lines 1866–1868](file:///C:/Users/miche/latex/algebra-1-ai-transcription-fall-2026/content/step4-2026-11-24-tuesday-week11-algebra-1-offset-final.tex#L1866-L1868):** Write `\operatorname{Im}(\bar{\phi}) = \operatorname{Im}(\phi) = k(\beta)` at `L1866` (matching the board note `writes: \operatorname{Im}(\phi) = k(\beta)` at `L1855` and speech `L1851` *"maybe called $\bar{\phi}$, but it's still $\phi$"*) and `$\bar{\phi} \colon K \xrightarrow{\sim} k(\beta)$ (the $\phi$ of \cref{thm:uniqueness-root-extension})` at `L1868`.
  2. **[Line 1762](file:///C:/Users/miche/latex/algebra-1-ai-transcription-fall-2026/content/step4-2026-11-24-tuesday-week11-algebra-1-offset-final.tex#L1762):** Cite `\cref{thm:universal-property-polynomial-ring}` (matching Wednesday line 378).

---

### W11-L6. Notation, Precision & Commutative-Diagram Polish in Wednesday (Wed)

- **Locations in [step4-2026-11-25-wednesday-week11-algebra-1-offset-final.tex](file:///C:/Users/miche/latex/algebra-1-ai-transcription-fall-2026/content/step4-2026-11-25-wednesday-week11-algebra-1-offset-final.tex):**
  1. **`\id_k` $\to$ `\operatorname{Id}_k$ ([lines 384](file:///C:/Users/miche/latex/algebra-1-ai-transcription-fall-2026/content/step4-2026-11-25-wednesday-week11-algebra-1-offset-final.tex#L384) & [1177](file:///C:/Users/miche/latex/algebra-1-ai-transcription-fall-2026/content/step4-2026-11-25-wednesday-week11-algebra-1-offset-final.tex#L1177)):** Matches `\operatorname{Id}` across the rest of the book and `Id` on the board (`L372`).
  2. **Terminology bridge for "degree of the extension" ([line 648](file:///C:/Users/miche/latex/algebra-1-ai-transcription-fall-2026/content/step4-2026-11-25-wednesday-week11-algebra-1-offset-final.tex#L648)):** Add one sentence noting that $\dim_k E$ is also called the \newterm{degree} of the field extension (matching the subsection title at `L627` and spoken *"degree of the extension"* at `L977`).
  3. **Indexed reference in distinctness parenthetical ([line 877](file:///C:/Users/miche/latex/algebra-1-ai-transcription-fall-2026/content/step4-2026-11-25-wednesday-week11-algebra-1-offset-final.tex#L877)):** Name **Step 2** in the parenthetical on line 877 so *"contradicting linear independence"* explicitly refers to the indexed implication $\hat{c}_{ij} = 0$ proved in Step 2 (for $\hat{c}_{ij} = 1, \hat{c}_{i'j'} = -1$, nonzero in every characteristic).
  4. **$\mathbb{Q}$-dimension equality in angle trisection ([line 1102](file:///C:/Users/miche/latex/algebra-1-ai-transcription-fall-2026/content/step4-2026-11-25-wednesday-week11-algebra-1-offset-final.tex#L1102)):** Note that the isomorphism of `\cref{thm:uniqueness-root-extension}` fixes $\mathbb{Q}$, so the $\mathbb{Q}$-dimensions agree.
  5. **Commutative-diagram arrow clearance ([lines 443, 454–455](file:///C:/Users/miche/latex/algebra-1-ai-transcription-fall-2026/content/step4-2026-11-25-wednesday-week11-algebra-1-offset-final.tex#L443)) & stale TikZ plan line ([line 927](file:///C:/Users/miche/latex/algebra-1-ai-transcription-fall-2026/content/step4-2026-11-25-wednesday-week11-algebra-1-offset-final.tex#L927)):** Change the bottom arrow start from `1.15` to `1.35` at `L443` (together with its two label `\path`s at `L454–455` and the `hidden` plan at `L424, L430`) to clear `$K = \faktor{k[x]}{(f)}$`, and update the stale `vertical bar` line in the `hidden` plan at `L927` to match the horizontal straightedge `(2.0, 0.8) -- (3.8, 0.8)`.

---

## 2. Dropped Items (Verified Against Board, Audio & Scope)

- **`W11-L1` ($V := \{ S \subset G \mid |S| = p^k \}$, Tue `L150–153`):** Dropped. Line 150 immediately precedes the display with *"let $V$ denote the set of all $p$-Sylow subgroups of $G$:"*, and the `aiNote` at lines 132–135 explicitly states that $\subset$ is the board's sign for both subsets and subgroups (`\cref{not:subset-board}`).
- **`W11-M3 (1)` ($\subset \mathbb{R}$ on $F_1 \subset \dots \subset F_k$, Wed `L987`):** Dropped. Frame `00:44:58` shows two separate towers on the board ($\mathbb{R}$–$E$–$\mathbb{Q}$ with $\alpha \in E$, and $E \subset F_1$–$F_2$–$\dots$–$F_k$–$\mathbb{Q}$ written top-down without $\mathbb{R}$). Moreover, the "if and only if" statement is mathematically true as stated: since $E \subset \mathbb{R} \subset \mathbb{C}$ and $\dim_{\mathbb{Q}} F_k = 2^k < \infty$, $F_k/E$ is algebraic so $F_k$ embeds over $E$ into $\mathbb{C}$, and any real number $\alpha \in E \subset \mathbb{R}$ lying in a complex quadratic tower over $\mathbb{Q}$ has constructible real/imaginary coordinates at each step ($\operatorname{Re}, \operatorname{Im}\sqrt{u + iv} = \pm\sqrt{(\pm u + \sqrt{u^2+v^2})/2}$), hence is constructible.
- **`W11-M3 (3)` ($(\Leftarrow)$ direction and $d > 0$ in `steps`, Wed `L1037–1045`):** Dropped. The `steps` box is explicitly scoped by its title `[Why Only Quadratic Extensions Arise]` to the $(\Rightarrow)$ direction argued by the lecturer (*"you can't do anything else"*; *"there's a little bit to prove"*), and *"whose solutions lie in $F_m$ or a degree-$2$ extension $F_{m+1} = F_m(\sqrt{d})$"* holds both for real intersection points ($d \ge 0$, with $d \in F_m^2$ giving $F_m$) and algebraically over $\operatorname{char}(F_m) = 0$.
- **`W11-L5 (3)` ("canonical relative to $\beta$", Tue `L1625, L1875`):** Dropped. `thm:uniqueness-root-extension` takes $\beta \in F$ as given in the hypothesis and explicitly states `(and sending $\alpha = \bar{x} \in K$ to $\beta \in k(\beta)$)` at line 1625.
