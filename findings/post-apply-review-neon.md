# Post-Apply Review: Applied Findings, Remaining Issues, and Newly Added Content (Gemini 4 Neon)

Checked 2026-11-23 by Gemini 4 Neon (High) on `HEAD` = `ce03919` (`algebra-1.pdf` at 745 pages).

Scope:
1. Verification of how Claude (Opus 5.5) applied the reviews in `findings/` (`speech-emdash-review-claude.md`, `speech-readability-review-claude.md`, `speech-readability-review-argon.md`) across commits `6bf0ad5`, `5875938`, `8c24f55`, and `e64997a`.
2. Automated and targeted checks for remaining issues across all 19 lectures (`content/step4-*.tex`), `content/prerequisites.tex`, `algebra-1.tex`, and `algebra-1.log`.
3. Review of the newly added content since the readability pass (`8df8f20`, `0a22eef`, `dcaddf2`, `ce03919`) and the recently added Week 10 lectures (`bd31593`, `52baf98`).

Line numbers refer to `HEAD` = `ce03919`.

---

## Short Answer

- **Applied findings:** Mostly applied accurately and conservatively. All mechanical invariants hold across the entire book (`0` LaTeX errors, `0` undefined references, `0` English `---,` / `---:` / `---;`, `0` unspaced dashes, `0` `uh`/`um` fillers in `speech` or `student`, `0` editor-voice tags like `spoken as` / `speaker says`). Claude also rightly rejected Argon's flawed suggestions (hallucinated A9 target sentence, tautological rewrite on W7 Wed:1184, word swap on W10 Tue:757, and altering `(application?)`).
- **Slips when applying findings:** Two Week 5 Wednesday edits inserted words (`this`, `doing`) that contradict the XHIGH rerun already in `reruns/week5-wed-xhigh-3parts/`; four unchanged C-items and three Neon-confirmed kept spots lack audit-trail entries/`% [WORD-CHECKED]` tags; and two open items in `speech-emdash-review-claude.md` (D9 on Week 10 Wednesday and the app half of D10) remain unclosed.
- **Concrete remaining bugs:** One **51.2 pt Overfull `\hbox`** in Week 10 Tuesday (the only overfull box in the entire 745-page PDF), one missed connector comma (`Of course I could...`), one missed post-dash repetition (`space --- ... --- space`), and two D9 leftover dashes still present in Week 10 Tuesday.
- **Newly added content:** `0a22eef`/`dcaddf2` (script $\mathscr{I}$ `aiNote`s) and `ce03919` (TOC header fix) work cleanly; `8df8f20` (stabilizer block matrix & Orbit-Stabilizer fractions) is solid apart from one minor parenthesis inconsistency on line 2076; the footnote settings in `ce03919` are harmless future-proofing (the book currently has `0` footnotes).

---

## 1. Verification of Applied Findings (`6bf0ad5`..`e64997a` and `findings/`)

### 1.1 Two Week 5 Wednesday edits contradict `reruns/week5-wed-xhigh-3parts/`

Neither Claude nor Argon checked `reruns/week5-wed-xhigh-3parts/step4-10-14-2026-wednesday-week5-Algebra_I-offset-final.tex` before inserting words in Week 5 Wednesday:

1. **C10 — `content/step4-2026-10-14-wednesday-week5-algebra-1-offset-final.tex:701–703`**
   - **Applied:** `So, is polynomial long division` $\to$ `So, this is polynomial long division`.
   - **Rerun witness (`reruns/week5-wed-xhigh-3parts/...:791`):**
     `Okay, so very important for us --- and I'm not going to review it because you definitely learned it in school, at least I think you did (I think I went to school, but it's been a long time since I remember) --- is polynomial long division`
   - **Issue:** `"is polynomial long division"` was not missing the subject `"this"`; it was the predicate of `"very important for us ... is polynomial long division"`, split onto a new paragraph by a Flash sentence break.
2. **Argon II.B.7 — `content/step4-2026-10-14-wednesday-week5-algebra-1-offset-final.tex:707`**
   - **Applied:** `so when division, you always have to assume` $\to$ `so when doing division, you always have to assume`.
   - **Rerun witness (`reruns/week5-wed-xhigh-3parts/...:793`):**
     `so in division you always have to assume somebody's not zero`
   - **Issue:** `"in division"` is much more likely what Flash misheard as `"when division"`; `"doing"` was invented without checking the rerun or audio.
3. *(Minor)* **C11 — `content/step4-2026-10-14-wednesday-week5-algebra-1-offset-final.tex:188`**
   - **Applied:** `--- so, what's this for? ---` $\to$ `--- so, what's this $(4)$? ---` without audio.
   - **Rerun witness (`reruns/week5-wed-xhigh-3parts/...:174–176`):** Omits the aside entirely before `Sorry. Sometimes we write this $(4)$ as $4\mathbb{Z}$`. Context strongly supports `$(4)$`, though a quick audio check would settle whether the aside was spoken at all.

### 1.2 Audit-trail gaps in `findings/speech-readability-review-claude.md` and `.tex` comments

1. **Four silently dropped C-items:** **C3** (W1 Wed:44), **C13** (W1 Wed:42), and **C15** lines 784 & 178 (W2 Wed) were left untouched (following Argon's "Keep as is") without being recorded under **Not applied** in `findings/speech-readability-review-claude.md` (lines 296–305).
2. **Missing `% [WORD-CHECKED]` tags on three Neon-confirmed kept spots:** Only the five *changed* blocks received `% [WORD-CHECKED (2026-11-22): ...]` comments. The three spots that Gemini Neon confirmed as spoken and that were kept unchanged carry no comment in the `.tex` files, inviting future reviews to re-flag them:
   - `content/step4-2026-09-16-wednesday-week1-algebra-1-offset-final.tex:921` (`That's a wider property.`)
   - `content/step4-2026-11-10-tuesday-week9-algebra-1-offset-final.tex:219` (`it's a very good answer.`)
   - `content/step4-2026-11-18-wednesday-week10-algebra-1-offset-final.tex:620` (`I'm just saying over what I've said already.`)

### 1.3 Open items in `findings/speech-emdash-review-claude.md`

1. **D9 on the first `prompt-engineering` `9b6915e` lecture (Week 10 Wednesday)** is still listed under **Open** (lines 402–406), even though Week 10 Wednesday has already been run and stored in `reruns/week10-wed-xhigh-3parts/`. Measuring it with `prompt-engineering\tools\speech-density.py --punct` gives:
   - `reruns/week10-wed-xhigh-3parts`: `30` blocks, `4,900` words, **`8.4` `---`/1k**, **`5` odd-dash sentences**, **`0` `---,`**, **`0.0` `;`/1k**.
   - `content/step4-2026-11-18-wednesday-week10-algebra-1-offset-final.tex` (the reviewed HIGH run in the book): `35` blocks, `4,841` words, **`8.7` `---`/1k**, **`8` odd-dash sentences**, **`0` `---,`**, **`0.0` `;`/1k**.
   - This confirms that `9b6915e` resolved the D9 leftovers on Stage 3.
2. **The app half of D10** (deterministic `---,` / `---:` / `---;` cleanup in `lec-extraction-prog`) is still open (not yet implemented in `C:\Users\miche\programming\lec-extraction-prog`).

---

## 2. Other Things That Need to Change

### 2.1 Concrete bugs / missed convention items

1. **51.2 pt Overfull `\hbox` (the only overfull box in the entire 745-page PDF)** — `content/step4-2026-11-17-tuesday-week10-algebra-1-offset-final.tex:1637–1639`:
   ```latex
   \begin{equation}\label{eq:binomial-mod-p-fixed-pts}
   \binom{n}{p^k} = |T| \equiv \#\text{fixed pts} \pmod{p} \qquad \text{(written on the board as } \binom{n}{p^k} = |T| = \#\text{fixed pts} \bmod p\text{)}.
   \end{equation}
   ```
   `algebra-1.log` reports `Overfull \hbox (51.23355pt too wide) detected at line 1639`. Moreover, the `aiNote` immediately below (lines 1647–1650, `Informal Congruence Signs on the Board`) already explains the board's `=` vs. `\equiv` notation. Remove the parenthetical from the numbered equation (or move it into prose/the `aiNote`).

2. **One missed connector comma** — `content/step4-2026-11-17-tuesday-week10-algebra-1-offset-final.tex:1759`:
   `Of course I could also pick this one` $\to$ `Of course, I could also pick this one` (matches the connector-comma sweep `65533fc`).

3. **Missed post-dash repetition and D9 leftover dashes in Week 10 Tuesday:**
   - `content/step4-2026-11-17-tuesday-week10-algebra-1-offset-final.tex:381`:
     `this is the space --- this is equal, definition --- space of left... set of left cosets of $H$ in $G$` (post-dash repetition `space --- ... --- space` plus false start, missed by both Claude and Argon).
   - Two of the exact D9 restart leftovers Claude cited in `findings/speech-emdash-review-claude.md` (lines 386–389) survived into the reviewed Week 10 Tuesday chapter:
     - Line `868`: `addition is well-defined in that group --- the addition is in this group`
     - Line `972`: `moves this element to there, and that element to there ... --- if I pick some $\alpha$ in $G$, then $\alpha$ maybe moves this element there, and that...`
     - *(Line `726` `my set $\widehat{T}$ --- and the hat means it's not...` also remains, though as a sentence-ending aside it reads naturally.)*

### 2.2 Optional book-wide consistency items (taste)

- **Semicolons in `speech` (Weeks 1–9):** Week 10 Tuesday and Wednesday have `0.0` semicolons/1k in `speech`, while Weeks 1–9 still have ~470 (book average `3.3`/1k, peaking at `7.0`/1k in W7 Tue) because semicolons were intentionally excluded from D11.
- **`Orbit-Stabilizer` vs. `Orbit--Stabilizer`:** Mixed across Weeks 9–10 (W9 Tue: `0`/`1`; W9 Wed: `13`/`12`; W10 Tue: `40`/`0`; W10 Wed: `1`/`18`).
- **Argon II.B.20 (`content/step4-2026-11-18-wednesday-week10-algebra-1-offset-final.tex:325`):** `Well, the stabilizer has a particular element $a_1$ in it` has no inline `(i.e., $X$)` (relying on the lecturer's follow-up sentence and the `aiNote` on line 336), whereas line 718 received an inline `(i.e., that divide)` despite also having an `aiNote` directly below. Adding `(i.e., $X$)` would make the two consistent.

---

## 3. Review of Newly Added Content (`8df8f20`, `0a22eef`, `dcaddf2`, `ce03919`, and Week 10)

### 3.1 `8df8f20` — Week 10 Tuesday stabilizer block matrix & Orbit-Stabilizer fractions
- **Block matrix (`content/step4-2026-11-17-tuesday-week10-algebra-1-offset-final.tex:2147, 2159`):** Dropping the vertical rule in the first row (`\multicolumn{1}{c}{1}`), removing the spoken-only `\overbrace{\ast \ \cdots \ \ast}^{\text{anything}}`, and updating the speech metanote on line 2147 are all clean and faithful to the board.
- **Orbit-Stabilizer box (`lines 2074–2079`):** Minor parenthesis inconsistency inside the same `content` box:
  - Lines `2074` and `2078` use double parentheses: `\operatorname{Stab}\bigl((1, 0, \dots, 0)^T\bigr)`.
  - Line `2076` (in between them) uses single parentheses: `\left|\operatorname{Orb}(1, 0, \dots, 0)^T\right|`.
  - Line `2074` also mixes the 4-row column vector on the LHS with `(1, 0, \dots, 0)^T` in the RHS denominator (intentional per the commit message, though slightly asymmetric on a single equation line). Standardizing line `2076` to `\left|\operatorname{Orb}\bigl((1, 0, \dots, 0)^T\bigr)\right|` would polish it.

### 3.2 `0a22eef` + `dcaddf2` — Set of ideals `aiNote`s (W4 Wed & W5 Tue)
- `content/step4-2026-10-07-wednesday-week4-algebra-1-offset-final.tex:415–421` and `content/step4-2026-10-13-tuesday-week5-algebra-1-offset-final.tex:138–143`:
  - Accurate, clear, and well-calibrated (`Some authors write $\mathcal{I}(R)$ or $\operatorname{Id}(R)$`).
  - Zero leftover `cl` symbols in either file; `\mathscr{I}` is used consistently (`46` occurrences in W4 Wed, `88` in W5 Tue). Nothing needs changing.

### 3.3 `ce03919` — Preamble TOC header fix & footnote settings (`algebra-1.tex:471–482`)
- **TOC `\markboth` override:** Verified directly in `algebra-1.pdf`. Page 2 (`Contents`, `plain` style) shows `1/ 744` centered in the footer; pages 3–15 show `CONTENTS` in the top-left header only and nothing in the footer; page 16 transitions cleanly to `Prerequisites`.
- **Footnote settings (`\interfootnotelinepenalty=10000`, `\setlength{\skip\footins}{16pt plus 4pt minus 2pt}`):** Harmless future-proofing carried over from `algebra-1-book-fall-2026`. Note that `algebra-1.tex` and `content/*.tex` currently contain **`0` `\footnote` commands**, so the inline comment (`a split one broke inside a word`, `which touched displayed equations and tall fractions`) describes a symptom from the textbook repo rather than this PDF.

### 3.4 Week 10 Tuesday & Wednesday overall
- Aside from the three items in Section 2.1 (`W10 Tue:1638` overfull box, `W10 Tue:1759` missing comma, `W10 Tue:381` post-dash repetition) and the two D9 leftover dashes (`W10 Tue:868, 972`), both lectures are clean (`0` semicolons, `0` `---,`, `0` undefined refs, well-checked against board frames and reruns).

---

## Method

- Word-diffed `5560299..e64997a` across all 18 touched lecture files and verified each item from `speech-readability-review-claude.md` and `speech-readability-review-argon.md` against `HEAD` (`ce03919`).
- Cross-checked Week 5 Wednesday and Week 10 Wednesday edits against `reruns/week5-wed-xhigh-3parts/` and `reruns/week10-wed-xhigh-3parts/`.
- Ran automated regex/LaTeX audits across all 19 lectures, `content/prerequisites.tex`, `algebra-1.tex`, and `algebra-1.log`, plus `prompt-engineering\tools\speech-density.py --punct --files` on `content/` and `reruns/`.
- Verified TOC headers/footers directly on `algebra-1.pdf` using `pypdf`.
