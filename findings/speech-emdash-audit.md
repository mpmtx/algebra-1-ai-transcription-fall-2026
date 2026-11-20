# Speech & Em-Dash (`---`) Audit — Algebra I Book

**Date:** 2026-11-20  
**Scope:** All 17 lecture chapters in `content/step4-2026-*-algebra-1-offset-final.tex` (`HEAD` = `0db7ab4`, compared against pre-Hydrogen baseline `f68edb4`), all pipeline stages (`step1`–`step4`) in `D:\lecture-videos\Algebra_I\extracted_output*`, and the Stage 1/3/4 prompts in `C:\Users\miche\latex\prompt-engineering\`.

---

## Executive Summary

The lecturer's `speech` blocks in the Algebra I book hit an **uncanny valley**: raw, halting spoken restarts and false starts are preserved verbatim and then decorated with heavy literary/German punctuation — especially `---` em-dashes (often unpaired, stacked 3+ times in a single sentence, or paired with German-only `---,` / `---:` / `---;`), plus bursts of semicolons (`;`) and mechanical `So,` commas.

This is **not** caused by running speech refinement multiple times (Stage 4 barely touches `speech`, and Week 4 Tuesday's "step 5" was only a PDF compilation repair, not a second speech refinement).

Instead, it is a **two-part interaction between the prompts and the Gemini 4 Hydrogen XHIGH switch in Weeks 7–9**:

1. **The prompts over-prescribe `---` and leak German `---,` / `---:` punctuation into English.** `speech-refinement.md` contains **212 inline `---`**, **36 mentions of `em-dash`/`em dash`**, and **24 occurrences of `---,`**, while forbidding Stage 3 from dropping or rephrasing spoken false starts.
2. **Gemini 4 Hydrogen obeys those instructions hyper-literally starting at Stage 1** — emitting **12–25 `---` per 1,000 words** (`200–320` per lecture) in raw verbatim transcription, compared to **0.1–2.4 `---` per 1,000 words** for Gemini 3.8 Flash.
3. **Weeks 1–6 vs. Weeks 7–9 were merged in opposite ways:**
   - **Weeks 1–6** kept the reviewed Flash-base book and only patched audio-verified fixes/clauses from the Hydrogen XHIGH rerun (`0c1cb4e`–`65db32f`). Speech style barely changed (only a few minor splicing blemishes).
   - **Weeks 7–9** threw out the Flash base and **replaced the entire chapter base with the Hydrogen XHIGH Step 4 output** (`386fb16`, `3947fad`), causing a **3× to 6× jump in `---` density** overnight at Week 7.

---

## 1. Whole-Book Metrics: Pre-Hydrogen (`f68edb4`) vs. `HEAD` (`0db7ab4`)

Counts cover text inside `\begin{speech}...\end{speech}` with `\inlinemetanote{...}` stripped. `odd/even/3+` counts sentences with an unpaired (odd) number of `---`, a paired (even, $\ge 2$) number, and sentences containing 3 or more `---`.

| Chapter | Base in `HEAD` | `f68edb4` `---` (/1k) | `HEAD` `---` (/1k) | `HEAD` odd/even/3+ | `---,` | `f68 ;` → `HEAD ;` | `f68 ...` → `HEAD ...` | `So,` |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| `09-16` W1 Wed | Flash 3.8 + check | 56 (8.9) | 56 (8.9) | 20 / 17 / 1 | 0 | 22 → 22 | 31 → 31 | 58 |
| `09-22` W2 Tue | Flash 3.8 + check | 89 (7.4) | 91 (7.5) | 37 / 26 / 1 | 0 | 60 → 60 | 33 → 33 | 45 |
| `09-23` W2 Wed | Flash 3.8 + check | 39 (6.8) | 39 (6.7) | 15 / 12 / 0 | 0 | 31 → 31 | 24 → 25 | 55 |
| `09-29` W3 Tue | Flash 3.8 + check | 115 (10.0) | 117 (10.1) | 73 / 21 / 1 | 0 | 29 → 29 | 26 → 26 | 56 |
| `09-30` W3 Wed | Flash 3.8 + check | 54 (8.9) | 54 (8.9) | 12 / 20 / 1 | **14** | 22 → 22 | 26 → 26 | 62 |
| `10-06` W4 Tue | Flash 3.8 + check | 67 (5.3) | 69 (5.5) | 19 / 23 / 2 | 0 | 30 → 30 | 79 → 81 | 143 |
| `10-07` W4 Wed | Flash 3.8 + check | 65 (10.7) | 65 (10.7) | 13 / 24 / 2 | **9** | 32 → 32 | 24 → 24 | 80 |
| `10-14` W5 Tue | Flash 3.8 + check | 75 (6.5) | 75 (6.5) | 15 / 30 / 0 | 4 | 35 → 35 | 34 → 37 | 61 |
| `10-15` W5 Wed | Flash 3.8 + check | 22 (3.6) | 22 (3.6) | 4 / 9 / 0 | 4 | 8 → 8 | 46 → 46 | 101 |
| `10-20` W6 Tue | Flash 3.7 + check | 49 (4.5) | 53 (4.7) | 15 / 17 / 2 | 4 | 28 → 30 | 45 → 47 | 143 |
| `10-21` W6 Wed | Flash 3.8 | 37 (6.9) | 37 (6.9) | 11 / 12 / 1 | 6 | 13 → 13 | 9 → 9 | 66 |
| **`10-27` W7 Tue** | **Hydrogen XHIGH** | **34 (2.8)** | **217 (16.6)** | **101 / 51 / 7** | **25** | **17 → 84** | **83 → 35** | **163** |
| **`10-28` W7 Wed** | **Hydrogen XHIGH** | **36 (5.6)** | **85 (12.8)** | **23 / 29 / 2** | **21** | **10 → 24** | 39 → 36 | 106 |
| **`11-03` W8 Tue** | **Hydrogen XHIGH** | **56 (4.6)** | **170 (12.9)** | **62 / 47 / 7** | **9** | **16 → 39** | **46 → 26** | **171** |
| **`11-04` W8 Wed** | **Hydrogen XHIGH** | **21 (3.5)** | **79 (12.8)** | **47 / 16 / 0** | 0 | 9 → 7 | **27 → 6** | 82 |
| **`11-10` W9 Tue** | **Hydrogen XHIGH*** | 112 (8.6)* | 112 (8.5) | **60 / 26 / 0** | 2 | 17 → 17 | 18 → 18 | **163** |
| **`11-11` W9 Wed** | **Hydrogen XHIGH*** | 80 (12.0)* | **86 (13.3)** | **40 / 20 / 3** | **8** | 22 → 11 | 25 → 20 | 88 |

*\*Week 9 was already on a Hydrogen base at `f68edb4` (`3947fad`). For comparison, the original Flash run of `11-10` in `extracted_output` had `1` `---` at Stage 1 and `81` (`6.9/1k`) at Stage 3.*

**Total `---,` occurrences across the book:** **102** (concentrated in W7 Tue: 25, W7 Wed: 21, W3 Wed: 14, W4 Wed: 9, W8 Tue: 9, W9 Wed: 8).

---

## 2. Pipeline Stage-by-Stage Breakdown (`step1 → step2 → step3 → step4`)

Comparing the same lectures across `D:\lecture-videos\Algebra_I\extracted_output` (Flash) and `extracted_output_xhigh_longdecode_*` (Hydrogen XHIGH):

| Lecture & Run | Stage 1 (`extract`) | Stage 3 (`speech-refinement`) | Stage 4 (`last-refinement`) |
|---|---|---|---|
| **W7 Tue — Flash** (`3.8-flash` / `3.7-flash`) | `14` `---` (1.0/1k) · `163` `...` · `3` `;` · `0` `---,` | `34` `---` (2.8/1k) · `83` `...` · `17` `;` · `0` `---,` | `34` `---` (identical) |
| **W7 Tue — Hydrogen XHIGH** (`300k_2parts`) | **`275` `---` (19.9/1k)** · `30` `...` · `48` `;` · `0` `---,` | **`217` `---` (16.8/1k)** · `35` `...` · **`83` `;`** · **`25` `---,`** | `217` `---` (identical) |
| **W8 Tue — Flash** (`3.8-flash`) | `4` `---` (0.3/1k) · `106` `...` · `0` `;` · `0` `---,` | `56` `---` (4.7/1k) · `46` `...` · `16` `;` · `0` `---,` | `56` `---` (identical) |
| **W8 Tue — Hydrogen XHIGH** (`300k_2parts`) | **`206` `---` (14.4/1k)** · `166` `...` · `42` `;` · `0` `---,` | **`170` `---` (13.0/1k)** · **`26` `...`** · `39` `;` · **`9` `---,`** | `170` `---` (identical) |
| **W6 Tue — Flash** (`3.8-flash` / `3.7-flash`) | `28` `---` (2.0/1k) · `83` `...` · `0` `;` | `49` `---` (4.6/1k) · `44` `...` · `28` `;` | `49` `---` (identical) |
| **W6 Tue — Hydrogen XHIGH** (`300k_2parts`) | **`208` `---` (15.6/1k)** · `150` `...` · `23` `;` | **`190` `---` (15.7/1k)** · **`16` `...`** · **`72` `;`** | `190` `---` (identical) |
| **W9 Tue — Flash** (`3.8-flash`) | `1` `---` (0.1/1k) · `52` `...` · `0` `;` | `81` `---` (6.9/1k) · `21` `...` · `24` `;` | `81` `---` (identical) |
| **W9 Tue — Hydrogen XHIGH** (`200k`) | **`312` `---` (24.8/1k)** · `29` `...` · `14` `;` | `112` `---` (8.6/1k) · `18` `...` · `17` `;` | `112` `---` (identical) |
| **W10 Tue — Hydrogen HIGH** (`300k_2parts`) | **`145` `---` (9.1/1k)** · `208` `...` · `21` `;` | **`137` `---` (10.4/1k)** · **`37` `...`** · `29` `;` | `137` `---` (identical) |

### What Each Stage Actually Does

- **Stage 1 (`extract`) — Origin of the Hydrogen `---` flood:**
  - `gemini-3.8-flash` rarely uses `---` in verbatim transcription (`0.1–2.4/1k`), preferring `...` and commas.
  - `gemini-4-hydrogen` (both `HIGH` and `XHIGH`, across every single Algebra lecture W1–W10) follows `environments-speech.md` (`L27–29`, `L164–170`) hyper-literally and emits **`12–25` `---` per 1k words** (`153` in W1 Wed, `320` in W3 Tue, `275` in W7 Tue, `312` in W9 Tue), turning every stutter, pause, abandoned phrase, and micro-aside into `---`.
- **Stage 2 (`merge`) — Neutral passthrough:**
  - Keeps punctuation unchanged aside from deduplicating part-overlap boundaries.
- **Stage 3 (`speech-refinement`) — Amplifier and lock-in:**
  - On **Flash** inputs, Stage 3 *introduces* `---`, `---,`, and `---:` (pushing W1–W6 from `~1/1k` up to `4–10/1k`).
  - On **Hydrogen** inputs, Stage 3 inherits 200–315 `---`, refuses to clean up raw restarts because the prompt forbids dropping words or rewriting stumbles, **converts remaining `...` into `---`** (e.g., W8 Tue `...` collapses `166 → 26`), and adds German-style `---,` (`0 → 25` in W7 Tue, `0 → 9` in W8 Tue) and `;` (`48 → 83` in W7 Tue).
  - **Concrete transformation in Week 8 Tuesday (`[00:02:19 - 00:03:27]`):**
    - *Hydrogen Stage 1:* `The second is that if I take $x$... let's say, I take $a$ and $b$ in the image, we should check --- we must check --- that $a$ times $b$ is in the image ... let $x$ and $y$ in $G_1$ be such that... let's go over here $f(x) = a$`
    - *Hydrogen Stage 3 / Book `HEAD` (`content/step4-2026-11-03-tuesday-week8-algebra-1-offset-final.tex` L176):* `The second is that if I take --- let's say, I take $a$ and $b$ in the image, we should check --- we must check --- that $a$ times $b$ is in the image ... let $x$ and $y$ in $G_1$ be such that --- let's go over here \inlinemetanote{...} --- $f(x) = a$`
    - Stage 3 dropped `$x$`, swapped `...` for `---`, kept the trivial self-correction `we should check --- we must check ---`, and wrapped `let's go over here` in another `---` pair.
  - **Smoking gun from Hydrogen's Stage 3 thinking log** (`D:\lecture-videos\Algebra_I\extracted_output_xhigh_longdecode_300k_2parts\10-27-2026-tuesday-week7-Algebra_I\step3-10-27-2026-tuesday-week7-Algebra_I-offset-speech_refined-thoughts.md`, 63k chars): Hydrogen repeatedly fixates on em-dash rules throughout the lecture (`"Applying Em-dash Rules"`, `"Confirming Em-dash Strategy"`, `"Implementing Em-dash Strategy"`, `"I'm focused on the em-dash"`, `"I have removed the extra words and I'm adding --- in this block"`).
- **Stage 4 (`last-refinement`) — Neutral on `speech`:**
  - `---` counts are identical to Stage 3 across all tested runs.

---

## 3. Merge Quality Audit: Weeks 1–6 vs. Weeks 7–9

### Weeks 1–6 (Selective Rerun-Check Patches, `0c1cb4e`–`65db32f`)

- **Overall verdict:** The speech merges in Weeks 1–6 were **not** the main culprit. Each commit changed at most 0–4 `---` occurrences, preserving the Flash speech base and only patching audio-verified omissions, slips, and timestamps.
- **Minor splicing / formatting blemishes spotted in Weeks 1–6:**
  - `content/step4-2026-09-16-wednesday-week1-algebra-1-offset-final.tex` L151: broken cut-off word with em-dash (`con---`).
  - `content/step4-2026-10-07-wednesday-week4-algebra-1-offset-final.tex` L419: `---;` and `---:`.
  - `content/step4-2026-10-14-tuesday-week5-algebra-1-offset-final.tex` L458: restored clause from `5c5ad71` creates a double opening (`Okay, so, we still have to prove the other way, which is... So, now the other way:`); L365, L466, L992, L1380, L1908 use `---:`.
  - `content/step4-2026-10-20-tuesday-week6-algebra-1-offset-final.tex` L425: restored aside from `e65fd17` has missing space / abrupt cut (`definition of unique factor--- so, actually`).

### Weeks 7–9 (Wholesale Hydrogen XHIGH Base Replacement, `386fb16` / `3947fad`)

- **Overall verdict:** Switching the full chapter base to Hydrogen XHIGH in `386fb16` is the direct reason Weeks 7–9 feel noticeably choppier and more dash-ridden than Weeks 1–6 (and than the pre-`386fb16` Flash editions of Weeks 7–8).
- **Malformed no-space em-dashes also survived in Weeks 7–9:**
  - `content/step4-2026-10-28-wednesday-week7-algebra-1-offset-final.tex` L432: `Now, that's the reflexive--- no, yeah, that's the reflexive property`
  - `content/step4-2026-11-10-tuesday-week9-algebra-1-offset-final.tex` L261 (`is equal to--- if`), L860 (`not---`), L945 (`the flips are--- I'll draw`), L947 (`are---`).

---

## 4. Exact Prompt Rules Causing the Weird Speech

Prompt pressure counts (excluding Markdown horizontal rules):

| Prompt file | Inline `---` | Mentions of `em-dash`/`em dash` | `---,` |
|---|---:|---:|---:|
| `transcription/environments/environments-speech.md` | 17 | 6 | 2 |
| `speech-refinement/speech-refinement.md` | **212** | **36** | **24** |
| `last-refinement/last-refinement.md` | 24 | 1 | 2 |

### Five Specific Prompt Culprits

1. **Stage 1 explicitly encourages `---` during verbatim transcription** (`environments-speech.md` L27–29, L164–170):
   - Tells Stage 1 to use `---` for self-interruptions, abrupt shifts, immediate vocabulary corrections, and parenthetical side-remarks, plus `---,` before subclauses. Flash ignored this; Hydrogen obeyed it 200–320 times per lecture.
2. **Stage 3 instructs gluing false starts and hanging clauses with `---` instead of cleaning them** (`speech-refinement.md` L118 Core Directive 2, L302 §1, L1723):
   - Example in prompt: `If I have a sequence $x_k$ --- now, we have seen this...` and *"Absorb false-starts into em-dashes instead of rewriting."*
   - Combined with Core Directive 9 (`L127`, `L460`, tightened in `0f6fb41` / `e7746f9`), Stage 3 becomes afraid to drop broken fragments and freezes them behind unpaired `---` (`101` unpaired in W7 Tue, `73` in W3 Tue, `62` in W8 Tue, `60` in W9 Tue):
     - `Let $I$ --- I have to prove it's a PID` (`10-27` L225)
     - `Then this is --- now, this is the part for you, exercise ... Prove $I$ --- what am I going to write here?` (`10-27` L251)
     - `Sorry --- these rings are all PIDs` (`10-27` L265)
     - `we first select --- choose --- some $x$ in $G_1$` (`11-03` L199)
     - `So, this is something that --- and it has matrix multiplication` (`11-03` L275)
3. **Stage 3 pushes `---` *instead of* commas for short appositives & asides** (`speech-refinement.md` L126 Core Directive 8, L526–538 §5, English Examples 3 & 6 with 15 and 19 `---` each):
   - Produces choppy interruptions like `So, it turns out this --- Gaussian integers --- is a PID` (`10-27` L181) and stacked multi-dash sentences like `the other is by a homomorphism --- this is way one ---, and the second way is a homomorphism $\sigma$ --- I should write the $\sigma$ a little better so it doesn't look like my $G$ ---, the $\sigma$ from this` (`11-11` L185).
4. **German `---,` and `---:` punctuation rule leaked into English** (`speech-refinement.md` L304, L530–537, L2083–2099):
   - Placing a comma after a closing *Gedankenstrich* (`---,`) is a German Duden rule. `speech-refinement.md` L537 explicitly prescribes it in English (*`"That is exactly what we imagine when we write down this formula --- that it is transitive ---, but here it is simply a formula."`*), and L2083–2099 model `---:`. Both look ungrammatical and jarring in English (`102` `---,` across the book, e.g. `10-27` L142: `--- there's a huge study of these rings, and this course is only the very beginning of this study ---, but at least you'll know`).
5. **Blanket English `So,` comma rule** (`speech-refinement.md` L493–504, `last-refinement.md` L15):
   - Forces a comma after every `So` (`163–171` times per Tuesday lecture), creating stiff/clunky spoken prose like `Okay, so, the last lecture...`, `and so, this says...`, `So, proof.`.

---

## 5. Recommended Next Steps

### A. Prompt Fixes (`C:\Users\miche\latex\prompt-engineering`)

1. **`environments-speech.md` (Stage 1):** Remove `---` (and `---,`) from Stage 1's active toolkit so verbatim transcription uses commas and `...` instead of flooding Hydrogen outputs with 200+ em-dashes up front.
2. **`speech-refinement.md` (Stage 3):**
   - Make `---,` **German-only**; explicitly forbid `---,`, `---:`, and `---;` in English (use a closing `---` alone, or commas/parentheses).
   - Dial back `---` frequency and examples: reserve `---` for genuine mid-sentence tangents, **at most one pair per sentence**, never for 1–2 word appositives (`this, the Gaussian integers,`), and never for trivial self-corrections (`we should check --- we must check ---` → `we must check`) or empty false starts (`if I take --- let's say, I take` → `if I take, let's say, $a$ and $b$`).
   - Clarify the interaction between Core Directive 2 (hanging clauses) and Core Directive 9 (don't drop content): a discarded 1–3 word restart that adds no content (`Let $I$ ---`, `Then this is ---`, `So, this is something that ---`) should be dropped rather than frozen behind an unpaired `---`.
   - Soften the English `So,` rule so `Okay, so` / `and so` / `So` as a casual spoken lead-in does not get forced into `Okay, so,`.
   - Update `last-refinement.md` L15 to stay aligned on the `So,` rule.

### B. Book Cleanup (`C:\Users\miche\latex\algebra-1-ai-transcription-fall-2026`)

1. **Priority 1 — Weeks 7–9 (`10-27` through `11-11`):** Targeted punctuation/readability pass inside `\begin{speech}` blocks only (preserving every `\inlinemetanote`, `\cref`, `(Recall: ...)`, `(i.e., ...)`, timestamp, and verified spoken word/slip):
   - Strip all English `---,` (replace with clean `---` or commas).
   - Fix malformed no-space dashes (`reflexive---`, `to---`, `not---`, `are---`).
   - Resolve stacked `3+ ---` sentences and awkward unpaired false-start `---` into clean commas, periods, or trimmed restarts.
2. **Priority 2 — Weeks 1–6 (`09-16` through `10-21`):**
   - Strip all `---,` (37 occurrences across W3 Wed, W4 Wed, W5, W6), `---:` / `---;` (W4–W5), and malformed no-space dashes (`con---` in W1 Wed, `factor---` in W6 Tue).
   - Spot-clean the `73` unpaired `---` in Week 3 Tuesday and the double opener in Week 5 Tuesday (`L458`).
