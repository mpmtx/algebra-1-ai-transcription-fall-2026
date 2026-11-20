# Speech em-dashes: what holds in the audit and in Argon's reply, and what both missed

Checked 2026-11-20 by Claude (Opus 5.5). Subject: [`speech-emdash-audit.md`](speech-emdash-audit.md) (the audit,
2026-11-20, untracked) and Gemini Argon's reply to it (pasted in chat on 2026-11-20, not saved in the repo). Book at
`HEAD` = `0db7ab4`, compared with `f68edb4`; pipeline outputs in `D:\lecture-videos\Algebra_I\extracted_output*`;
prompts in `C:\Users\miche\latex\prompt-engineering` at `ca15f0e`, and their history. Line numbers refer to these
versions.

This file restates every finding of the audit (A1) and of Argon's reply (B1) that holds up, so it can be read on its
own. What does not hold is in A2 and B2, my own findings in C, one merged list of what to do in D, and the numbers
in the tables at the end.

## Short answer

The audit is right about *what* happened. Weeks 7–9 were rebased on the Gemini 4 Hydrogen XHIGH rerun (`386fb16`,
`3947fad`), which brought in 410 of the 420 dashes the book gained since `f68edb4`. The dashes are born in
Hydrogen's Stage 1, and Stage 4 leaves them alone. The prompt rules it names (`---,` with an English example, dashes
instead of commas around asides, dashes for false starts) exist and are worth changing. Every dash count it gives
reproduces.

It is wrong or incomplete about *why*, and that changes where the fix should go:

1. **It is not literal obedience.** The Flash run and the Hydrogen run of Week 7 Tuesday got the same punctuation
   rules (dashes, `---,`, semicolons, false starts), at Stage 1 and at Stage 3; other rules changed in between (C1).
   Hydrogen also breaks Stage 1 rules that ask for *less* punctuation: clause-linking semicolons, which Stage 1
   forbids (39 in Week 7 Tuesday, Flash 3); dashes at plain restarts, where Stage 1 asks for `...` or commas;
   dashes without their spaces (260 `word--- ` in Week 9 Tuesday). It punctuates like an editor at the verbatim
   stage. The dash rules give it room but do not explain the flood.
2. **Hydrogen's Stage 3 removes dashes, it does not amplify them.** In Weeks 6–8 it kept about 70% of the dashes it
   was given, so 74–86% of the dashes in its output are Stage 1's; in Week 9 Tuesday it removed 77%. The amplifier is
   *Flash's* Stage 3, which added 20–80 dashes per lecture, mostly where a comma stood.
3. **Stage 3's prompt does not forbid cleaning up false starts; it says three different things about them** (L25,
   L302, L460), and two of its examples disagree (L292, L536). Stage 3 keeps a dash that looks like an aside, and most
   of Hydrogen's do.
4. **`So,` is not part of the Week 7 jump.** The Flash editions had as many (Week 7 Tuesday: 208 at `f68edb4`, 163
   now), and in the Flash runs Stage 4 added most of those commas.

So the fix with the most leverage is in Stage 3: one consistent rule for false starts, and dashes in its input
treated as raw marks to judge, not as approved asides. Changing Stage 1 alone will not do it, since Hydrogen already
ignores explicit Stage 1 prohibitions. The mechanical part (`---,` in English) is better fixed by a script than by
one more prompt sentence.

Argon's reply agrees with everything in the audit, its errors included. Of its four additions, the semicolon point
holds and the `---,` safety net holds in aim. The `\inlinemetanote` "parking spot" and the cut-off/dash conflation
explain little of what is in the book.

## How this was checked

- **Counts:** my own script, not the audit's. Speech is the text between `\begin{speech}` and `\end{speech}`, with
  `%` comments and `\inlinemetanote{...}` (balanced braces) removed; `;`, `...` and `So,` are counted outside inline
  math. Words are whitespace tokens with each `$...$` counted as one, so my rates per 1,000 words run 5–10% above the
  audit's (Week 7 Tuesday: 18.2 against 16.6). The counts themselves compare directly.
- **Sentences** end at `.`, `?` or `!` before a capital, digit, `\`, `(` or math, and at a blank line. *Odd* means a
  sentence with an odd number of `---` (at least one unpaired dash), *even* two or more paired ones, *3+* three or
  more.
- **Stage 2 → Stage 3:** each speech block aligned with its counterpart, token by token (`difflib`). A dash is *kept*
  if it sits in an unchanged stretch, otherwise *removed* or *added*. For an added dash, the punctuation that stood
  there before is recorded.
- **Prompt versions:** the Stage 3 prompt as sent, from each run's `step3-*-prompt-log.md`; Stage 1's rules from the
  prompt repo's history at the run's date.
- **Citations and logs:** each of the audit's 20 book citations looked up at `HEAD`; the Week 7 Tuesday run logs
  read for its Stage 3 attempts.
- **Not done:** no audio heard, no judgement of individual dashes as right or wrong, no prompt change tried. The
  scripts were throwaway; the description above is enough to redo every count. Strip math within a line: three
  malformed `$` in Week 9 Tuesday's Flash Stage 3 otherwise hide 2 `;` and 1 `...`.
- **Second opinions:** Gemini 4 Hydrogen XHIGH checked this file against the repos and the pipeline folders
  (2026-11-20, review only, and it quoted the last sentence as proof of reading). It found seven slips, all checked
  and corrected here: the prompts of the two Week 7 runs differ outside the punctuation rules (C1), the
  unspaced-dash counts (C3), the origin of `factor---` (A2.10, B2.3), a missing chapter in B1.1, Stage 4's copy of
  the note rule (B2.2), the `So` count (C4) and two cells of T2. It did not see Argon's reply, so B1 and B2 were
  checked against the sources only. Gemini 4 Neon, which wrote the audit, read this file too (seen by the user).

## A. The audit's findings

### A1. Holds (restated)

1. **Not repeated refinement.** Stage 3 and Stage 4 have the same `---` count in all eight runs checked, so Stage 4
   leaves the dashes alone. Week 4 Tuesday's "step 5" is a Flash "PDF repair after step 4/4" of 2026-10-11 (chapter
   header L14–24), not a second speech refinement. It did re-emit the whole document (50k output tokens), so "only a
   compile repair" describes its task rather than guarantees its effect; Week 4 Tuesday is among the least
   dash-dense chapters, so it is not a source either way.
2. **Weeks 1–6 kept the reviewed Flash base.** The checks against the Hydrogen rerun (`0c1cb4e`–`65db32f`) changed
   each chapter's speech dashes by 0 to +4 (`e65fd17`, Week 6 Tuesday: 49 → 53) and its `---,` not at all.
3. **Weeks 7–9 were rebased on the Hydrogen XHIGH Step 4 output.** Speech dashes per commit: `386fb16` Week 7 Tue
   34 → 217, Week 7 Wed 36 → 85, Week 8 Tue 56 → 170, Week 8 Wed 21 → 79, Week 9 Wed 80 → 86; `3947fad` Week 9 Tue
   81 → 112. The `---,` came with it: 0 → 25, 21, 9, 0 and 8 in `386fb16`. Week 9 Wednesday was already a Hydrogen
   (200k) base at `f68edb4`, so `f68edb4` is "pre-Hydrogen" for Weeks 1–8 only, as the audit's asterisk says.
4. **The metrics reproduce:** every per-chapter `---` count at `HEAD` and at `f68edb4`, the `...` counts, the `---,`
   per chapter, and the pattern of unpaired dashes (my sentence split gives 97/53/7 for Week 7 Tuesday against the
   audit's 101/51/7). In all: 1,007 dashes at `f68edb4`, 1,427 at `HEAD`; 410 of the 420 more come from `386fb16`.
   Table T1.
5. **Hydrogen's Stage 1 is where the Hydrogen dashes are born.** Stage 1 `---` per lecture: Hydrogen 145–320 (Week 1
   Wed 153, Week 3 Tue 320, Week 6 Tue 208, Week 7 Tue 275, Week 8 Tue 206, Week 9 Tue 312, Week 10 Tue at HIGH
   145), Flash 1–28 (Week 6 Tue 28, Week 7 Tue 14, Week 8 Tue 4, Week 9 Tue 1). Table T2.
6. **Stage 2 passes them through**, removing only the part-overlap duplicates (Week 7 Tuesday: 275 → 260, with 5%
   fewer words).
7. **On Flash input, Stage 3 is what makes the dashes,** and the `---,` and `---:`: Week 7 Tue 14 → 34, Week 8 Tue
   4 → 56, Week 9 Tue 1 → 81 (with 18 `---,`).
8. **The prompt rules it names exist, at the lines given:**
   - `speech-refinement.md` L537 (§5) prescribes `---,` in an *English* example: "That is exactly what we imagine
     when we write down this formula --- that it is transitive ---, but here it is simply a formula." L304 (§1) states
     the `---,` rule for every language, and L2083–2099 model `---:` (German examples). The comma after a closing
     dash is German (Duden) usage; English drops it, and the closing dash takes its place. The English example has
     been in the prompt since 2026-06-30 (`6e373e1`).
   - Core Directive 8 (L126): "Use LaTeX em-dashes (`---`) for conversational asides or parenthetical thoughts
     instead of sandwiching them in commas."
   - Core Directive 2 (L118) and §1 (L302) resolve a false start by keeping it and marking the break with a dash.
     L1723: "Absorb false-starts into em-dashes instead of rewriting."
   - The English `So,` rule: `speech-refinement.md` L493–504, `last-refinement.md` L15.
   - Pressure in numbers: `environments-speech.md` has 17 inline `---`, 6 mentions of em-dash and 2 `---,`;
     `speech-refinement.md` 212, 36 and 24 (and 4 `---:`); `last-refinement.md` 24, 1 and 2.
9. **The examples are real and at the cited lines** (19 of 20; A2.7 has the miss). They include `we should check ---
   we must check ---` (Week 8 Tue L176; the Hydrogen run's Stage 1 L129 has the same words), `we first select ---
   choose --- some` (L199), `Let $I$ --- I have to prove it's a PID` (Week 7 Tue L225), `So, it turns out this ---
   Gaussian integers --- is a PID` (L181), and `---,` at Week 7 Tue L142 and Week 9 Wed L185.
10. **Blemishes in Weeks 1–6:**
    - `con---` (Week 1 Wed L151);
    - `---;` (Week 4 Wed L419);
    - `---:` (Week 5 Tue L365, L466, L992, L1380, L1908);
    - a double opening after a restored clause (Week 5 Tue L458);
    - `factor--- so, actually` (Week 6 Tue L425).

    No-space dashes in Weeks 7–9: `reflexive---` (Week 7 Wed L432), and `is equal to---`, `not---`, `the flips are---`
    and `are---` (Week 9 Tue L261, L860, L945, L947).
11. **Book cleanup, Weeks 7–9 first:**
    - Weeks 7–9: all English `---,`, the no-space dashes, sentences stacked with 3+ dashes, unpaired dashes after
      empty restarts.
    - Weeks 1–6: `---,`, `---:`, `---;`, `con---`, `factor---`, Week 3 Tuesday's unpaired dashes and Week 5 Tuesday's
      double opening.

    Agreed, with the counts of A2.6 (D11).

### A2. Does not hold, or needs correcting

1. **"Gemini 4 Hydrogen obeys those instructions hyper-literally starting at Stage 1."** The punctuation rules were
   the same for both runs (C1), and Hydrogen breaks the Stage 1 rules that would have meant less punctuation (C3). Stage 1 itself
   calls `...` "The Primary Tool" (L135) and dashes "allowed" (L166); only the aside rule (L29) says "use". The
   better description: Hydrogen's own habit, which the dash rules permit.
2. **"Stage 3 — amplifier and lock-in ... refuses to clean up raw restarts because the prompt forbids dropping
   words or rewriting stumbles."**
   - On Hydrogen input, Stage 3 is a net remover. Week 7 Tue 260 → 217, Week 8 Tue 198 → 170, Week 6 Tue 200 → 190,
     Week 9 Tue 297 → 112. Removed: 73, 55, 59 and 228 dashes; added: 30, 27, 49 and 43.
   - The prompt does not forbid cleaning up:
     - Directive 2: "You must fix clear grammatical errors, stumbles, and severe filler-word loops."
     - Directive 5: "Your job is to remove stutters and fix grammar."
     - L25: false starts "disappear".
     - L310: a cut-off fragment is dropped.
     - Example 5 (L292): "only the corrected word stays".

   What the prompt does is contradict itself (C2). "Lock-in" is right in one sense: Stage 3 keeps most of the spaced
   dashes it is given.
3. **"Converts remaining `...` into `---` (e.g., W8 Tue `...` collapses 166 → 26)."** Of the 27 dashes Stage 3 added
   in Week 8 Tuesday, 16 took the place of an ellipsis. In Week 7 Tuesday none did; 19 of its 30 replaced a comma.
   The ellipses disappear because Stage 3 deletes restarts and stutters together with their `...`, and the dashes
   fell too (198 → 170).
4. **"Clarify the interaction between Core Directive 2 and Core Directive 9"** (5.A.2, third bullet: drop a 1–3 word
   restart that adds no content). The drop rule is already there (L25, Directive 9 L127, L460). The prompt needs its
   contradicting passages removed (C2, D1), not one more rule.
5. **The "smoking gun" thinking log belongs to an attempt that never reached the book.**
   `step3-...-speech_refined-thoughts.md` (63k characters, started 01:02:29) is the first Stage 3 attempt of Week 7
   Tuesday. It aborted at request 2/10 on the daily quota ("Schritt 2 (Speech Refinement) fehlgeschlagen. Breche
   Pipeline ab."). `lecx finish` reran Stage 3 from the Stage 2 file at 01:12, and the output header names
   `...-thoughts-2.md`. None of the five quoted phrases is in that file, but it mentions em-dashes 72 times (C6), so
   the conclusion stands on the right file.
6. **Numbers.**
   - The book's `---,` total is 106: the audit's own table adds up to 106, while its text says 102. Weeks 1–6 have 41,
     not 37.
   - The jump at Week 7 is 2.4× (Week 7 Wed) to 6.4× (Week 7 Tue) by count, not "3× to 6×".
   - "Every single Algebra lecture W1–W10 ... 12–25 `---` per 1k" does not fit Week 10 at HIGH: 145 dashes, 9.1/1k by
     the audit's own table.
7. **One citation:** Week 4 Wednesday L419 has the `---;`, but no `---:`; the chapter's two `---:` are at L383 and
   L754.
8. **`So,` is not part of the Week 7 jump.**
   - The Flash editions had as many: Week 7 Tue 208 at `f68edb4` against 163 now, and the book as a whole 1,648 →
     1,661.
   - In the Flash runs Stage 4 inserted most of these commas (C4).
   - Stage 1 has the rule too (`environments-speech.md` L191), which the audit's culprit 5 leaves out.

   The `So,` question concerns the whole book and is a style decision of its own (D7).
9. **"Stage 4 (`last-refinement`) — neutral on `speech`."** It is neutral on dashes only. It adds connector commas in
   speech by design (`last-refinement.md` L11 and L15; C4).
10. **The no-space dashes have three different origins** (B2.3):
    - `con---` is a broken word. Today's prompt writes that as `con-`, and Stage 3 drops it.
    - `factor---` is in no stage of either Week 6 Tuesday run. The Flash run has `unique factor- so, actually`, and
      the Hydrogen rerun `unique factorization --- well actually`. It was typed into the book when the passage was
      restored in `e65fd17`.
    - The four in Week 9 Tuesday and `reflexive---` are restarts in Hydrogen's left-attached `word--- ` style (C3).

## B. Argon's reply

### B1. Holds (restated)

1. **The Week 7 cliff is a merge-strategy artifact, not damage from repeated passes:**
   - Weeks 1–6 kept the Flash base and took only checked clauses and slips from the rerun.
   - Weeks 7–9 took the rerun as their base (= A1.1–A1.3).

   Its passage comparison is right: `f68edb4` had "we first select, choose some $x$ in $G_1$" (Week 8 Tue L207) and
   "So, it turns out this ring of Gaussian integers is a PID" (Week 7 Tue L184), where `HEAD` has `we first select ---
   choose --- some $x$` and `this --- Gaussian integers --- is a PID`. Its third example does not contrast: "---
   that's the homomorphism property ---" already had its dashes at `f68edb4` (Week 8 Tue L188).
2. **`speech-refinement.md` contradicts itself on false starts.**
   - L25 and L460 drop them ("a fragment the lecturer says again right after, or one that says nothing on its own").
   - Directive 2 (L118) and §1 (L302) resolve them with `word --- word`.
   - Directive 8 (L126) asks for dashes instead of commas around asides.

   Confirmed; C2 adds two more pairs of rules that disagree.
3. **Stage 3 keeps a dash it is handed.** In Weeks 6–8, 74–86% of Stage 3's dashes are Stage 1's, at the same place,
   which supports this. One qualification: where Stage 1's dash visibly marked a repeat, as in most of Week 9
   Tuesday's `the--- the`, Stage 3 did remove it (228 of 297). So it keeps the dashes that look like asides. Those
   include the short fragments followed by *different* words (`Let $I$ --- I have to prove`), which is where the
   unpaired dashes in the book come from.
4. **`---,` is a German (Duden) rule that leaked into English.** `speech-refinement.md` L530–537 teaches it for every
   language and models it in an English sentence at L537; in English the closing dash absorbs the comma (= A1.8).
5. **The `So,` rule is in all three stages:** `environments-speech.md` L191, `speech-refinement.md` L493–504,
   `last-refinement.md` L15. Correct as stated; A2.8 says why it is a separate question.
6. **Restrain semicolons (addition 3).** `speech-refinement.md` §2 L474 ("Use a semicolon to connect two complete,
   independent clauses that are deeply logically linked, when no conjunction is used") and §1 L304 invite
   clause-linking semicolons in English speech. In Hydrogen's Weeks 6–7 they doubled or tripled from Stage 1 to
   Stage 3 (Week 7 Tue 39 → 74, Week 6 Tue 23 → 72; outside math), and lecturers' quick clauses read like essay prose
   as a result.
   Agreed. Two corrections:
   - "Nearly 5×" holds only for Week 7 Tuesday against Flash's Stage 3; it is 2.4× in Week 8 and 2.6× in Week 6.
   - Many of Hydrogen's semicolons are already in its Stage 1 (C3), so Stage 3 must also turn them back, not only stop
     adding them.
7. **Keep `---,` out with checks, not only with prompt text (addition 4).** `prompt-engineering\tools\prompt-lint.py`
   exists and is the right place to keep English `---,`, `---:` and `---;` out of the prompts' examples. For the
   output, a deterministic fix beats one more line in Stage 4's prompt (D10).

### B2. Does not hold

1. **"Every factual claim holds up."** See A2.
2. **The `\inlinemetanote` "parking-spot" effect (addition 1)** does not explain the flood:
   - The count is about right: 28 of Week 7 Tuesday's 217 dashes follow a note directly (Argon: 24).
   - The share is not higher than in the Flash chapters: 13%, against 16% (Week 1 Wed), 33% (Week 2 Wed), 15% (Week 3
     Tue) and 20% (Week 4 Wed). In Hydrogen's Stage 1 it is 8%.
   - Even all 28 together would explain only 28 of the 183 dashes Week 7 Tuesday gained.
   - The rule ("an em-dash ends a part like a period: the note goes before the dash") places a note before a dash
     that is there already; it creates none.
   - It has been in force since 2026-10-26 (`9b05bc8`), so the Flash run of Week 7 Tuesday had it too (4 of its 14
     dashes follow a note).
   - Both citations are right: the rule is in `environments-inlinemetanote.md` L43–45, and `last-refinement.md` L95
     is Stage 4's copy ("an em-dash ends a part like a period, so the note goes before it"). Stage 3 has it too.
3. **"Malformed no-space dashes come from confusing the adjacent Em-dash and Cut-off Word rules" (addition 2)**
   explains none of the six as a pipeline error:
   - `factor---` looks like that confusion, but no stage of either Week 6 Tuesday run has it. It was typed into the
     book during the rerun check (`e65fd17`), from the Flash run's `factor- so` (A2.10).
   - `con---` entered the book on 2026-10-09 (`f8e1024`), two weeks before the cut-off rule existed (`72d2f25`,
     2026-10-23).
   - `reflexive---` and the four in Week 9 Tuesday are not broken words. They are restarts in the left-attached style
     that Hydrogen's Stage 1 used hundreds of times in some runs (C3), against the prompt's spacing rule.

   Removing `---` from Stage 1 may still help, but Hydrogen already ignores that spacing rule.

## C. New findings

1. **Same punctuation rules, different model.**
   - **Stage 3:** the prompt as sent on 10-29 (Flash, Week 7 Tue), 11-13 (Hydrogen, Week 9 Tue) and 11-14
     (Hydrogen, Week 7 Tue) has 212 inline `---`, 24 `---,`, 4 `---:` and 36 mentions of em-dash each time. Between
     10-29 and 11-14 other rules changed: an anchor for an unclear word, note placement, the math handoff, and the
     `overview` description. The dash, `---,`, semicolon, `So,` and false-start rules did not change, apart from the
     notation (`` ` --- ` `` written `` `word --- word` ``). The rule that a note goes before a dash was in both
     (since 2026-10-26). 11-13 and 11-14 are identical.
   - **Stage 1:** 52 commits restructured `transcription/` between 10-29 and 11-14. Its dash rules (aside dashes
     with `---,`, "Em-dashes are allowed", ellipsis "The Primary Tool") still read the same on 10-29
     (`transcription.md` L819, L982, L1011 at `406133b`) and 11-14 (`environments-speech.md` L27, L135, L164 at
     `92f8bf3`), apart from the same notation change. They date from June/July 2026, so every Flash run had them.
   - **What did change between the two Week 7 Tuesday runs:** the model (3.8 Flash → 4 Hydrogen), the thinking
     level (Stage 1 HIGH → XHIGH, Stage 3 MEDIUM → XHIGH), the parts (4 → 2) and the non-punctuation rules above.
     The comparison cannot separate these, but it does rule out a change in the punctuation rules.
2. **Stage 3's prompt contradicts itself about false starts, in four places:**

   | Keeps the false start | Drops it |
   |---|---|
   | §1 L302: "resolve it minimally using punctuation (such as colons or em dashes `word --- word`) to separate the false start from the clean continuation" | L25: "Only fillers, stutters, false starts (a fragment the lecturer says again right after, or one that says nothing on its own) and repeated words disappear" |
   | L460: such a fragment "may go too ... When unsure, keep it" (added 2026-10-29, `e7746f9`) | L25's "disappear" |
   | §5 L536, English example: "This forms a closed set --- or rather, a compact set --- in $\mathbb{R}^n$" (both words kept) | Example 5, L292: for "from $m$, uh, from the ciphertext", "only the corrected word stays" |
   | L1723, heading: "Absorb false-starts into em-dashes instead of rewriting" | the same example: it drops `wir werden das...` and puts dashes only around the real aside |

   The book's examples follow the left column: `we should check --- we must check ---` and `we first select ---
   choose ---` (L536); `Let $I$ --- I have to prove it's a PID` and `Then this is --- now, this is the part for you`
   (L302).
3. **Hydrogen breaks Stage 1's rules towards more punctuation:**
   - **Semicolons.** Stage 1 (L151): "Do not use semicolons to link independent clauses in verbatim transcription."
     Hydrogen's Stage 1 speech has 39 (Week 7 Tue), 41 (Week 8 Tue), 23 (Week 6 Tue) and 70 (Week 3 Tue). Almost
     all link clauses: "a very nice proof actually; it used ...", "This is not one; you have to actually have some
     ideas", "the set of bijections; I hope that's clear". Flash's Stage 1: 0–3.
   - **Dashes at plain restarts.** Stage 1 wants commas for a repetition (L183) and `...` for a looping false start
     (L137, L142–144). Hydrogen writes `---`: 3–7% of its Stage 1 dashes in Weeks 6–8 (`we --- we can't apply`), 22% in
     Week 9 Tuesday (`in the--- in the proof`).
   - **Spacing.** L166 asks for `word --- word`. In speech blocks, Hydrogen's Stage 1 wrote `word--- ` (attached on
     the left) 260 times in Week 9 Tuesday, 210 in Week 3 Tuesday and 103 in Week 5 Tuesday, and `word---word` 23
     times in Week 8 Tuesday. Week 7 Tuesday has none, and Week 2 Tuesday 2. In Week 9 Tuesday, Stage 3 respaced or
     removed all but four: the four the audit lists.
4. **Stage 4 writes the `So,` commas into speech.** `last-refinement.md` L11 lets it fix "a missing comma after an
   introductory connector" in speech, and L15 is the rule.
   - Flash, Week 7 Tuesday: Stage 3 has `So` without a comma 199 times (198 `So ` and one `So...`) and `So,` 10
     times. Stage 4 has `So,` 208 times: it put the comma after all 198, leaving only the `So...`. `so,` goes 1 → 79.
   - Other Flash runs: Stage 4 added 89 (Week 6 Tue) and 79 (Week 8 Tue) lowercase `so,`.
   - Hydrogen runs: Stage 4 added 18 (Week 6 Tue) and 16 (Week 7 Tue).
5. **Stage 3 cleans up much more when the dashes look like restarts.** Week 9 Tuesday got the same Stage 3 prompt as
   Week 7 (C1). Its Stage 1 dashes were mostly attached restarts, and Stage 3 removed 228 of 297. In Weeks 6–8, where
   Stage 1's dashes are mostly spaced and look like asides (Week 8 Tuesday: 23 of 206 unspaced; 3–7% plain
   restarts), it removed 28–30%. Same prompt, so the look
   of the input decides. This is why D2 tells Stage 3 how to read the dashes it is given.
6. **Hydrogen's Stage 3 thinks about dashes; Flash's does not.** The used Stage 3 attempt of Week 7 Tuesday mentions
   em-dashes 72 times in 85k characters of thought summaries, and the aborted attempt 110 times in 64k. Flash's Week 7
   Tuesday Stage 3 mentions them 0 times in 32k.
7. **Stage 3 hears the audio.** The finish run uploads the lecture's `.aac` and attaches it at Stage 3. A Stage 3
   rerun with a changed prompt can therefore work on an existing Stage 2 file and still check against the
   recording, which makes it a cheap test of a prompt change before the book is touched (D9).
8. **The app adds no dash guidance of its own.** There is no em-dash text in `lec-extraction-prog\src`, so a prompt
   fix lives in `prompt-engineering` alone.

## D. What to do

**Status (2026-11-20):**

- **Done** in `prompt-engineering` `179c9e2`: D1–D6, D8, and the lint half of D10. Stage 2's punctuation table was
  synced too. Stage 1 now restricts dashes to asides and deliberate reformulations, as D6 asked; repairs and
  restarts get `...`. The change was reviewed twice by Gemini 4 Hydrogen.
- **Done** in the book, in the commit that adds this line: D11 and the book half of D10, in all 17 chapters.
  - Every speech sentence with a dash was read and judged by the rules now in Stage 3 §5:
    - a dash pair stays around a real aside;
    - a restart that repeats its words, and a near-synonym repair, go with their dash (28 fragments, such as `Let
      $I$ ---`, `we should check ---` and `select ---`);
    - a broken-off sentence keeps its words and ends with `...`;
    - short appositions and second pairs became commas or parentheses;
    - `---,` lost its comma, and `---:` and `---;` were rewritten.
  - Slips the lecturer marks himself ("sorry") stayed. No word was added, and every `\inlinemetanote`, `\cref`,
    `(Recall: ...)` and `(i.e., ...)` is still there (script check against the previous commit).
  - Speech dashes went 1,427 → 1,185, `---,`/`---:`/`---;` 116 → 0, unspaced 7 → 0, and sentences with 3+ dashes
    30 → 0. Sentences with an odd count went 551 → 435 (the tool's own sentence split, hence 551 rather than T1's
    549).
  - Most of what remains odd is an aside or comment at the end of a sentence, which the rules allow. Week 3 Tuesday's
    73 were nearly all of that kind and needed only 7 edits.
  - Semicolons were not part of D11; three in Week 4 Tuesday became periods while splitting a four-dash sentence.
  - Gemini 4 Hydrogen XHIGH reviewed the whole applied diff before the commit (212 hunks in all 17 chapters, review
    only, last hunk header quoted as proof). Its three findings held and were fixed: a comma after a closing
    parenthesis (Week 6 Tue L393), an `if` dropped with a restart (Week 8 Tue L176), and `we usually` dropped
    although it makes a point (Week 9 Tue L1540). It did not see those three fixes or this status block.
- **Open:**
  - D7 (`So,`, a separate style decision).
  - D9: Week 10 Tuesday's Stage 3 failed on the quota on 2026-11-20 and has to be rerun anyway; that rerun is the
    first one with the new prompt. It was restarted at 12:37 and hit "high demand" errors at first.
  - The app half of D10.
  - Week 5 Tuesday's double opening (L458) has no dash, and a review had restored the clause, so it was left as it
    is.

Prompts (`prompt-engineering`), most leverage first:

1. **Stage 3, false starts: one rule, L25's.** A fragment the lecturer says again right after, or one that says
   nothing on its own, disappears.
   - L460: say the same; keep "When unsure, keep it" only for a broken-off sentence that makes a point.
   - §1 L302: drop the false start instead of separating it with a dash.
   - §5: show the trivial repair dropped (`we should check --- we must check` → `we must check`); keep the
     closed/compact example only as a correction that changes the meaning, and say so.
   - L1723: give the heading what its example shows.
2. **Stage 3, the dashes it is given.** Say that `---` in the input is Stage 1's raw mark, judged like any other
   punctuation:
   - a dash pair stays only around a real aside;
   - a dash after an empty or repeated fragment goes with the fragment;
   - an unpaired dash that only marks a restart becomes nothing, a comma or a period.
3. **`---,` German only** (audit, Argon).
   - Drop the English example at L537.
   - In §1 L304 and in §5, say that in English the closing dash takes the comma's place, and that `---:` and `---;`
     do not occur.
   - Make the same change to Stage 1's aside rule (`environments-speech.md` L29), which is language-neutral now.
4. **Directive 8 (L126) and §5** (audit): dashes only for long or interrupting asides; a short appositive stays
   between commas (`this ring, the Gaussian integers, is a PID`); at most one dash pair per sentence.
5. **Semicolons** (Argon): English speech uses `;` as a super-comma only, as German does (§2 L474, §1 L304). Since
   Hydrogen's Stage 1 already writes clause-linking ones, Stage 3 turns them into a period or a comma.
6. **Stage 1** (audit): restrict `---` to real asides, or drop it from the verbatim toolkit. Put the existing rules
   at the top of the punctuation section: repetition → commas, looping false start → `...`, broken word → `word-`.
   Expect only part of the effect with Hydrogen (C3), and measure it (D8). Editing `environments-speech.md` in
   place needs no change in the app; adding or renaming a Stage 1 file needs `Stage1PromptFiles.cs` edited and a
   Release rebuild.
7. **`So,`:** a style decision for the whole book, separate from this one. If it is softened, change it in all three
   stages (Stage 1 L191, Stage 3 L493–504, Stage 4 L11/L15).

Checks:

8. **Measure every run.** Extend `prompt-engineering\tools\speech-density.py` (it already counts fillers, repeats and
   cut-offs) with:
   - `---` per 1,000 words;
   - sentences with an unpaired dash;
   - `---,`, `---:`, `---;` and `;`.

   Run it on Stage 1 and Stage 3 and compare with T2.
9. **Test a prompt change cheaply.** Rerun Stage 3 alone on Week 7 Tuesday's existing Hydrogen Stage 2 file, as
   `lecx finish` did on 11-14 (`lecx refine run --tex ...step2-...-merged.tex --step 2 ...`; it costs requests), and
   compare with T2 before touching the book.
10. **Fix `---,` mechanically.** Replace `---,` → `---` (and `---:`, `---;`) in English speech with a script or in
    the app, not with another prompt instruction; `prompt-lint.py` keeps English `---,` out of the prompts' examples.

Book (the audit's plan, with corrected counts; Weeks 7–9 first):

11. **Edit speech blocks only, and only punctuation and empty restarts.** Every word that makes a point stays
    (Directive 9), spoken slips stay, and so do every `\inlinemetanote`, `\cref`, `(Recall: ...)`, `(i.e., ...)` and
    timestamp. The PDF is rebuilt in the same commit.
    - All English `---,`: 106, of which 65 in Weeks 7–9 and 41 in Weeks 1–6. Also `---:` (9, all in Weeks 4–5) and
      `---;` (1, Week 4 Wed L419).
    - The 7 no-space dashes (A1.10).
    - Sentences with 3+ dashes: 30, 19 of them in Weeks 7–9.
    - Unpaired dashes after empty restarts. Sentences with an odd count: Week 7 Tue 97, Week 3 Tue 73, Week 8 Tue 62,
      Week 9 Tue 58, Week 8 Wed 45, Week 9 Wed 40.
    - Week 5 Tuesday's double opening (L458).

## Tables

**T1. Speech in the book, `f68edb4` → `HEAD`** (my counts; rate per 1,000 words at `HEAD`)

| Chapter | Base | `---` (rate) | odd/even/3+ | `---,` | `;` | `...` | `So,` |
|---|---|---:|---:|---:|---:|---:|---:|
| 09-16 W1 Wed | Flash | 56 → 56 (9.6) | 20/17/1 | 0 | 22 → 22 | 31 → 31 | 57 → 58 |
| 09-22 W2 Tue | Flash | 89 → 91 (8.1) | 35/27/1 | 0 | 60 → 60 | 33 → 33 | 47 → 47 |
| 09-23 W2 Wed | Flash | 39 → 39 (7.6) | 13/13/0 | 0 | 31 → 31 | 24 → 25 | 54 → 55 |
| 09-29 W3 Tue | Flash | 115 → 117 (11.2) | 73/21/1 | 0 | 29 → 29 | 26 → 26 | 58 → 59 |
| 09-30 W3 Wed | Flash | 54 → 54 (9.6) | 12/20/1 | 14 | 22 → 22 | 26 → 26 | 62 → 62 |
| 10-06 W4 Tue | Flash | 67 → 69 (6.0) | 17/24/2 | 0 | 30 → 30 | 79 → 81 | 151 → 152 |
| 10-07 W4 Wed | Flash | 65 → 65 (11.7) | 13/24/2 | 9 | 32 → 32 | 24 → 24 | 80 → 80 |
| 10-14 W5 Tue | Flash | 75 → 75 (7.1) | 15/30/0 | 4 | 35 → 35 | 34 → 37 | 59 → 61 |
| 10-15 W5 Wed | Flash | 22 → 22 (3.9) | 2/10/0 | 4 | 8 → 8 | 46 → 46 | 101 → 101 |
| 10-20 W6 Tue | Flash 3.7 | 49 → 53 (5.0) | 13/18/2 | 4 | 28 → 28 | 45 → 47 | 143 → 144 |
| 10-21 W6 Wed | Flash | 37 → 37 (7.4) | 11/12/1 | 6 | 13 → 13 | 9 → 9 | 68 → 68 |
| 10-27 W7 Tue | Hydrogen | 34 → 217 (18.2) | 97/53/7 | 25 | 17 → 74 | 83 → 35 | 208 → 163 |
| 10-28 W7 Wed | Hydrogen | 36 → 85 (13.4) | 23/29/2 | 21 | 10 → 24 | 39 → 36 | 90 → 106 |
| 11-03 W8 Tue | Hydrogen | 56 → 170 (14.1) | 62/47/7 | 9 | 16 → 38 | 46 → 26 | 168 → 171 |
| 11-04 W8 Wed | Hydrogen | 21 → 79 (13.9) | 45/17/0 | 0 | 8 → 6 | 27 → 6 | 76 → 82 |
| 11-10 W9 Tue | Hydrogen* | 112 → 112 (9.6) | 58/27/0 | 2 | 17 → 17 | 18 → 18 | 163 → 163 |
| 11-11 W9 Wed | Hydrogen* | 80 → 86 (14.8) | 40/20/3 | 8 | 21 → 9 | 25 → 20 | 63 → 89 |
| **Book** | | **1,007 → 1,427 (10.2)** | **549/409/30** | **106** | **399 → 478** | **615 → 526** | **1,648 → 1,661** |

\* Already Hydrogen at `f68edb4`. Week 9 Tuesday's Flash edition (`d076faf`) had 81 dashes and 18 `---,`.

**T2. The pipeline, Flash and Hydrogen runs of the same lectures** (speech only; S1–S4 = Stages 1–4)

| Run | `---` S1 → S2 → S3 → S4 | S2 → S3 kept / removed / added | `---,` S3 | `;` S1 → S3 | `...` S1 → S3 | `so,` S3 → S4 |
|---|---:|---:|---:|---:|---:|---:|
| W6 Tue, Flash 3.7 | 28 → 26 → 49 → 49 | not computed | 4 | 0 → 28 | 83 → 44 | 1 → 90 |
| W6 Tue, Hydrogen XHIGH | 208 → 200 → 190 → 190 | 141 / 59 / 49 | 43 | 23 → 72 | 150 → 16 | 31 → 49 |
| W7 Tue, Flash 3.8 | 14 → 14 → 34 → 34 | 14 / 0 / 20 | 0 | 3 → 17 | 163 → 83 | 1 → 79 |
| W7 Tue, Hydrogen XHIGH | 275 → 260 → 217 → 217 | 187 / 73 / 30 | 25 | 39 → 74 | 30 → 35 | 15 → 31 |
| W8 Tue, Flash 3.8 | 4 → 4 → 56 → 56 | 4 / 0 / 52 | 0 | 0 → 16 | 106 → 46 | 3 → 82 |
| W8 Tue, Hydrogen XHIGH | 206 → 198 → 170 → 170 | 143 / 55 / 27 | 9 | 41 → 38 | 166 → 26 | 9 → 9 |
| W9 Tue, Flash 3.8 | 1 → 1 → 81 → 81 | 1 / 0 / 80 | 18 | 0 → 24 | 52 → 21 | 2 → 14 |
| W9 Tue, Hydrogen XHIGH 200k | 312 → 297 → 112 → 112 | 69 / 228 / 43 | 2 | 14 → 17 | 28 → 18 | 11 → 25 |

Added dashes in Flash's Stage 3 mostly took the place of a comma (19 of 20, 40 of 52, 48 of 80). Stage 1 alone,
Hydrogen: Week 1 Wed 153, Week 3 Tue 320, Week 10 Tue (HIGH) 145. Had Week 1 Wednesday been rebased too, its
Hydrogen Stage 3 (74 dashes, 17 `---,`) would have replaced the book's 56 dashes and 0 `---,`.
