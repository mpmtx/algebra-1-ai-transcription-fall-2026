# Speech blocks: what still reads oddly, and what is worth changing

Checked 2026-11-22 by Claude (Opus 5.5), on the book at `HEAD` = `e9c395c` (all reruns merged, dash and
connector-comma passes done). I read every `speech` and `student` block of the 19 lectures in full, with the
`\inlinemetanote`s stripped, and looked at the board notes wherever a sentence depends on them. Line numbers refer to
`content/step4-*.tex` at `e9c395c`. **Applied on 2026-11-22 together with Gemini Argon's review; what was applied,
what was not, and what waits for the audio is in the status section at the end.**

The question: is anything strange left in the speech blocks (weird sentences, repetitions, false starts) that is
worth changing in the book as it stands? The prompts are out of scope.

## Short answer

The speech is in good shape. It reads like a lively, lightly edited transcript, and most of what still looks rough
is the lecturer's own style (asides, jokes, self-corrections, complaints about the chalk), which should stay. What
is worth changing is small and local:

- **A. Leftovers of earlier editing passes** (9 items): mechanical, safe to fix without the audio.
- **B. Repetitions and restarts** a reader trips over (13 items): editorial, safe without the audio.
- **C. Sentences that are garbled or say something misleading** (17 items, some with two or three spots): most need the audio or a frame
  before changing; each has a candidate fix.
- **D. Asides that are authentic but noisy** (4 items): trimming is a matter of taste.
- **E. Looked at and would leave** (the rest, listed so nobody re-flags them).

W6 Wed has nothing to change; W3 Wed, W5 Tue and W7 Wed almost nothing.

## Lecture keys

| Key | File in `content/` |
|---|---|
| W1 Wed | `step4-2026-09-16-wednesday-week1-algebra-1-offset-final.tex` |
| W2 Tue | `step4-2026-09-22-tuesday-week2-algebra-1-offset-final.tex` |
| W2 Wed | `step4-2026-09-23-wednesday-week2-algebra-1-offset-final.tex` |
| W3 Tue | `step4-2026-09-29-tuesday-week3-algebra-1-offset-final.tex` |
| W3 Wed | `step4-2026-09-30-wednesday-week3-algebra-1-offset-final.tex` |
| W4 Tue | `step4-2026-10-06-tuesday-week4-algebra-1-offset-final.tex` |
| W4 Wed | `step4-2026-10-07-wednesday-week4-algebra-1-offset-final.tex` |
| W5 Tue | `step4-2026-10-13-tuesday-week5-algebra-1-offset-final.tex` |
| W5 Wed | `step4-2026-10-14-wednesday-week5-algebra-1-offset-final.tex` |
| W6 Tue | `step4-2026-10-20-tuesday-week6-algebra-1-offset-final.tex` |
| W6 Wed | `step4-2026-10-21-wednesday-week6-algebra-1-offset-final.tex` |
| W7 Tue | `step4-2026-10-27-tuesday-week7-algebra-1-offset-final.tex` |
| W7 Wed | `step4-2026-10-28-wednesday-week7-algebra-1-offset-final.tex` |
| W8 Tue | `step4-2026-11-03-tuesday-week8-algebra-1-offset-final.tex` |
| W8 Wed | `step4-2026-11-04-wednesday-week8-algebra-1-offset-final.tex` |
| W9 Tue | `step4-2026-11-10-tuesday-week9-algebra-1-offset-final.tex` |
| W9 Wed | `step4-2026-11-11-wednesday-week9-algebra-1-offset-final.tex` |
| W10 Tue | `step4-2026-11-17-tuesday-week10-algebra-1-offset-final.tex` |
| W10 Wed | `step4-2026-11-18-wednesday-week10-algebra-1-offset-final.tex` |

## A. Leftovers of earlier editing passes (fix)

**A1. W7 Tue:1455**, `Okay, so, far, the question is:` → `Okay, so far, the question is:`
The connector-comma pass (`65533fc`) split "so far". The only such break of a fixed phrase in the book (searched
`so, far`, `and so, on`, `so, to speak`, `so, that`; case-insensitive).

**A2. W8 Tue:265**, `So, much more interesting than that claim` → `So much more interesting than that claim`
Same cause: "so much" is an intensifier here, not the connector.

**A3. W2 Tue:1478**, `otherwise it would divide, so, long division says $r$ is between zero and $n$`
Grammatical, but the eye reads "so, long division" as a phrase. Optional: `otherwise it would divide; so long
division says ...` or `..., so the division algorithm says ...` (he said "division algorithm" two sentences
earlier).

**A4. W8 Tue:746**, `Because the even ones are $+1$ (speaker says \qt{one}), that's in the kernel.`
An editor's remark inside the speech. Saying "one" for $+1$ is not a slip worth marking: drop
`(speaker says \qt{one})`, or move it into a `%` comment.

**A5. W10 Tue:1425**, `I've just taken this $T$ (spoken as \qt{$P$}, i.e., $T$) and I've cut it up`
→ `I've just taken this $P$ (i.e., $T$) and I've cut it up`.
The book's slip convention is: the spoken word stays, the meant one follows in `(i.e., ...)`. This form inverts it
and adds an editor's voice.

**A6. W10 Tue:1731**, `the $p^k$-element subsets of $\widehat{T}$ (spoken as \qt{$T$}, i.e., $\widehat{T}$)`
→ `the $p^k$-element subsets of $T$ (i.e., $\widehat{T}$)`. Same as A5.
A4–A6 are the only "spoken as / speaker says / pronounced" remarks in speech blocks (W10 Wed:691 "pronounced" is in
an aiNote, where it belongs).

**A7. W10 Wed:109, 276, 670, 695, 862**, `Okay, so we start`, `Okay, so we're going to study`, `Okay, so this is
the action we'll consider`, `Okay, so what are we going to do`, `Okay, so we need to think` → `Okay, so, we ...`.
The book has `Okay, so,` 195 times and `Okay, so` + word only six times; these five in the last lecture miss
the comma of the connector-comma convention. (W10 Tue:862 `Okay, so far there's been no action` is right as it is.)

**A8. W2 Wed:1095**, `This great 20th-century Hungarian mathematician (i.e., Paul Erd\H{o}s) said that ...`
`(i.e., ...)` marks slips everywhere else; here it adds a name he did not say. The insight box right after the
block (1102) already names Erdős and gives the quote: drop the gloss.

**A9. W2 Tue:2017**, speech box `[01:11:29 - 01:12:07]` holds only a metanote (he erases the board). The only speech
box in the book without speech. Either keep it (it accounts for 38 seconds) or fold the note into the end of the
block before (1953). Taste.

## B. Repetitions and restarts (trim)

**B1. W4 Tue:1773, 1779, 1825, 1827, 1910**, `the Gaussian integers (i.e., Gaussian rationals $\mathbb{Q}[i]$)` five
times within a few minutes. The aiNote at 1811 explains his naming once. Keep the full gloss at 1773 and shorten the
other four to `(i.e., $\mathbb{Q}[i]$)`.

**B2. W9 Wed:1132, 1196, 1198 (twice), 1291, 1293**, `a divisor of $G$ (i.e., $|G|$)` six times, plus
`this $T$ (i.e., $|T|$)` at 1293. "Divides $G$" for the order is normal speech for a group theorist, and 1132 itself
goes on `the number of elements of $G$`. Keep the first gloss, drop the others.

**B3. W6 Tue:516**, `if $R$ is a PID (i.e., a UFD), then the polynomial ring is a U... Sorry, screwed up. Is a UFD,
then the polynomial ring is a UFD. Then the polynomial ring is a UFD.`
He corrects himself at once, so the gloss is redundant, and the last sentence doubles the one before.
→ `if $R$ is a PID, then the polynomial ring is a U... Sorry, screwed up. Is a UFD, then the polynomial ring is a
UFD.` (The WORD-CHECKED comment at 512 stays.)

**B4. W9 Tue:2505**, `So, it's something trivial (i.e., nontrivial) --- it's something nontrivial that's always
spinning $G$ around.` He corrects himself in the next breath, so the gloss is redundant: drop `(i.e., nontrivial)`.

**B5. W1 Wed:1217**, `Of course, if it's finite-dimensional, of course it has a basis.` → drop the second
`of course`.

**B6. W2 Wed:538**, `Yeah, $m$ is prime. $m$ is prime.` → `Yeah, $m$ is prime.`

**B7. W4 Wed:248**, `An example, for example: if you take $\mathbb{Z}$ goes to $\mathbb{Q}$` → `For example: if you
take ...`

**B8. W5 Wed:289**, `That's how that's how you're zero $\bmod I$ and $J$.` → `That's how you're zero ...`

**B9. W7 Tue:1599**, `Of course, the inverse of $e$ is, of course, $e$, right` → drop one `of course`.

**B10. W8 Wed:576**, `And the answer is yes, and what am I going to write for $\hat{y}$? And the answer is yes
\inlinemetanote{writes: YES}, and you got $\hat{y}$ equals what?` A restart that reads as a doubled sentence.
→ `And the answer is yes \inlinemetanote{writes: YES}. And what am I going to write for $\hat{y}$? You got $\hat{y}$
equals what?`

**B11. W10 Wed:925**, `But these... \inlinemetanote{pushes the lower board up ...} ...but these are really
incredibly cool arguments.` → `But these \inlinemetanote{...} are really incredibly cool arguments.`

**B12. W10 Tue:597**, `I can't see with the glare. Let's do it that way then. It's hard to see with the glare` →
drop one of the two glare sentences.

**B13. W5 Wed:534**, `Uh, but it's a confusing formula` → `But it's a confusing formula`. The only "uh/um" left
in a speech block. Student blocks keep them nine times (W2 Tue:454, 462, 486; W3 Tue:560; W5 Tue:1736; W8 Wed:263;
W9 Tue:1248; W10 Tue:1405, 2125). Pick one rule; I would drop them there too, since the speech is cleaned of
fillers everywhere else and the student lines are short enough that the fillers stand out.

## C. Garbled or misleading sentences (check the audio or a frame first)

Ordered by how much the reader is misled.

**C1. W9 Tue:628**, `It's not true, by the way, if you have a group of order $p$ times $q$, where $p$ and $q$ are
prime, it has to be cyclic, because, for example, $S_3$ has order $6$` — for a line it reads as asserting the
false statement. → `It's not true, by the way, that if you have ..., it has to be cyclic`. An editorial "that" is
safe even without the audio.

**C2. W10 Wed:556**, `It has size less than $p$ to the $k$ and greater than $p$ to the $k$, so it has size $p$ to
the $k$` — literally a contradiction; the board has $|\operatorname{Stab}(X_j)| \ge p^k$ and the earlier bound is
$\le$. → `at most $p$ to the $k$ and at least $p$ to the $k$`, or keep the words and add
`(i.e., at most ... at least)`.

**C3. W1 Wed:44**, `and then you can multiply it by $1$ (i.e., $(-i) \cdot i = 1$)` — "multiply it by 1" says
something trivial and the gloss has to rescue it. He means $i$ has the inverse $-i$. Audio; candidate `you can
multiply it to get $1$`.

**C4. W5 Wed:628**, `where $d$ is the coefficient of the highest not zero` — $d$ is the index (exponent) of the
highest non-zero coefficient. Unmarked slip: add `(i.e., the index of the highest non-zero coefficient)`.

**C5. W7 Tue:1916**, `I would get a power of $m$, $m$ lower, that's the neutral.` — garbled; meant: a lower power
of the element that is the neutral element (contradicting the minimality of $m$). Audio; candidate `I would get a
power lower than $m$ that's the neutral element`.

**C6. W4 Tue:560**, `$f$ takes the $1$ to $1$, that's the definition of a ring (Recall:
\cref{def:ring-homomorphism})` — slip for "ring homomorphism"; the Recall already points there. Add
`(i.e., ring homomorphism)` after "ring".

**C7. W4 Tue:1457**, `but now we quotient out by $f$, and then that's just the zero group` — meant: by
$\ker(f)$; the board note has $\faktor{\ker(f)}{\ker(f)} = 0$. Add `(i.e., $\ker(f)$)` after `$f$`.

**C8. W3 Tue:300**, `so, let's try this: $10\mathbb{Z}$, just to say a little bit.` — the example that follows is
the units of $\faktor{\mathbb{Z}}{10\mathbb{Z}}$ (subsubsection at 306); as written it names the ideal. Audio:
probably "Z mod 10 Z"; candidate `$\faktor{\mathbb{Z}}{10\mathbb{Z}}$`.

**C9. W5 Wed:1025**, `you take something from the $\mathbb{Z}$ side and something from the two side` — about the
non-principal ideal $(2, x)$ in $\mathbb{Z}[x]$; "the two side" makes no sense (the rerun heard "the $x$, he says,
$x^2$ side"). Audio; candidate `the $x$ side`.

**C10. W5 Wed:703**, `So, is polynomial long division \inlinemetanote{writes: Poly long div}.` — the subject is
missing. Audio; candidate `So, this is polynomial long division`. (The line before, `it's been a long time since I
remember, but...`, is odd but spoken; leave it.)

**C11. W5 Wed:188**, `to $\mathbb{Z} \bmod 4$ --- so, what's this for? --- and $\mathbb{Z} \bmod 6$` — the aside
makes no sense as written. Possibly `so, what's this, four?` (checking the number while writing). Audio.

**C12. W1 Wed:921**, `That's a wider property. These are the linear properties --- ... --- but this property is
about the multiplication.` — "wider" is odd; "weirder" would fit (the absorbing property of a kernel next to the
linear ones). Audio.

**C13. W1 Wed:42**, `And those confused our multiplication always, because you could always put in as many $-1$'s
and $+1$'s as you want.` — about units spoiling uniqueness of factorization; "confused our multiplication" is odd
(factorization?). Audio.

**C14. W2 Tue:117**, `if you look at this Metaphor page` and `That Metaphor page is there`; the board note has
`writes \qt{Metaphor 2018}`. A course page name that may be misheard (the board note is pipeline output too). A
frame settles it.

**C15. W2 Wed:784**, `So, the inertia of language:` and **W2 Wed:816**, `that argument comes from the norm in
complex analysis so that you prove it.` and **W2 Wed:178**, `We just discussed this last time, so, I wanted to
say.` — three odd spots in one lecture: a suspicious word ("inertia"; maybe right), a garbled ending, a trailing
ending. Audio.

**C16. W9 Tue:219**, `It's a strange question. So, the answer is that it's a very good answer.` (question?) and
**W9 Tue:319**, `or maybe it's a hard question, not the answer, but you should at least consider it` (candidate:
`maybe it's a hard question to answer, but you should at least consider it`). Audio.

**C17. W10 Wed:620**, `I'm just saying over what I've said already.` (candidate: `going over`) and **W10
Wed:866**, `maybe I should erase it, because I don't have... $x$ is fixed.` (the rerun has "because you remember
it"; still open from the rerun check). Audio.

## D. Authentic but noisy asides (taste)

**D1. W4 Wed:133–147** (`[00:04:21 - 00:05:34]`), a minute of microphone trouble: `Is that my phone? ... What aspect
of me is at fault? ... Can you hear me?` Could shrink to one sentence plus a metanote.

**D2. W10 Wed:295, 312, 327, 407, 554**, five remarks about managing the board and the chalk (`I'm not sure I'll be
able to pull it off` twice, `Ah, it's the pink one again`, `I keep getting the pink ones. I don't know what's... I
don't know. I give up.`, `I'm never going to do this again`). Each is fine; together they crowd the Sylow proof.
Keep one or two.

**D3. W7 Wed:95–97**, `but not always` three times in three sentences (plus `but not exclusively`). Natural; one
could go.

**D4. W3 Wed:862–866**, the "nought" joke (`I say \qt{nought} all the time ... That was a complicated joke.`) only
works if one hears "a-nought b-nought", which the book writes as $a_0 b_0$. Keep as is; a gloss would kill it.

## E. Looked at and would leave

- **(application?)** W1 Wed:1217 and **(notion?)** W2 Tue:2414: deliberate, each with a WORD-CHECKED comment after
  three hearings.
- **Replies to students the transcript cannot hear**: W1 Wed:656 (`maybe this is what you're hinting at`), W8
  Wed:979 (`It's a good question.`), W10 Tue:455 and 1140 (both already carry an "inaudible answer" metanote), W9
  Tue:1392 (`\qt{no} was the wrong answer. ... Yes, it's right.`, with a murmur note), W9 Tue:1102 (cut-off student,
  with a note).
- **W2 Tue:731–733** `if zero is in $H$`: the board says $0 \in H$ too, and the definition box explains it.
- **W5 Tue:1224** `the proposition from the first lecture`: proved at 552 in the same session; "first lecture"
  probably means the first hour of today's double lecture, and the statement follows at once.
- **W10 Tue:241**, four `(i.e., ...)` resolving "this" in one block: dense but useful.
- **W10 Wed:974**, `this one has order $p$ to the $\ell$ --- it has order $p$ to the $k$`: clear with the board note.
- **W8 Tue:2409** `Oh. This was wrong, by the way. Six, look.`, **W4 Tue:479** `Sorry.` (chalk slips),
  **W2 Tue:321** `Sorry, what are we doing here?`, **W2 Wed:675** `Nah.`, **W6 Tue:255** `Factorization domains.`
  (said while writing the topic), **W1 Wed:151** `this one becomes that` (the board note carries it), **W3
  Wed:622**, **W3 Tue:1850**, **W5 Wed:571**, **W9 Wed:268** `The third point`: authentic or clear in context.
- The lecturer's asides (Nietzsche, the Martian, Schopenhauer, Confucius, Catalan, the languages gag, the 500-page AI
  transcript in W8 Wed) carry the lectures. Leave them.

## Method

Speech and student blocks extracted per lecture with the metanotes removed (brace-counted), wrapped, and read in
order, lecture by lecture. Candidates were then located in the source by exact substring and their lines checked in
context; counts (`Okay, so,`, `So,`, um/uh, the glosses in B1/B2, speech boxes without speech) come from greps over
`content/step4-*.tex`. No audio was played and no frames were taken for this review: everything marked "Audio" in C
is unverified.

## Status, 2026-11-22: Argon's check, and what was applied

Gemini Argon reviewed this file and the 19 lectures: `findings/speech-readability-review-argon.md`, committed
unchanged in `5560299`. I checked each of its items against the source. The commit that adds this section applies
both reviews: 18 lecture files, 88 changed lines, every edit matched by its exact old text; PDF rebuilt (745 pages, no
errors, no undefined references).

### How Argon's file relates to this one

- Its proof of reading to the end is right (W10 Wed:1037).
- **Its Part I ("Verification of Claude's Findings") does not follow this file.** Its A1, A2, A4–A7, B10–B12, C1,
  C2, C5, C16 and C17 are spots this file never named; they are Argon's own finds, most of them good. Of this file's
  items it skips A2, B2, B4, B10–B12, C1, C2, C5, C16, C17 and D2/D3, and its Part II lists A1 and A7 as "missed by
  Claude".
- **It quotes rules that are not in `speech-refinement.md`:** a §3 sentence naming `Okay, so, / All right, so,`, a §4
  "maximum 2 `---` per sentence" and a §5 "never repeat the pre-dash word after the closing `---`". The two edits it
  bases on §5 (W6 Tue:220, W7 Tue:307) still hold under the real rule on looping restarts (line 449).
- Its version of A9 appends the note to a sentence that is not in the file (`All right, so, let me state these
  properties carefully.`; line 1962 is `You know this function, right?`).
- **Where it corrected this file:** C10 is line 702, not 703. W10 Wed misses the comma 14 times, not 5 (one more
  `Okay, so` at 599 and eight `All right, so`; the book has `All right, so,` 68 times). My semicolon option in A3
  breaks the Stage 3 semicolon rule. "Metaphor" (C14) is right: it is ETH D-MATH's course-page site,
  metaphor.ethz.ch. And "take this flight by $C$" (W10 Tue:496, flagged WORD-SUSPECT) matches the lecturer's own "the
  direct flight here" for following an arrow in W8 Tue:492.

### Applied

From this file: A1–A8 (A3 with a period, Argon's form; A4 writes `$1$`, as spoken), A7 at all 14 spots in W10 Wed,
B1–B13 (B4 keeps only "nontrivial", since Stage 3 drops a slip corrected at once; B13 in the student lines too, with
Argon's three small fixes there), C1, C2, C4 (my gloss, not Argon's "(i.e., exponent)"), C5 as a gloss, C6 (Argon's
form), C7, C8 (Argon's gloss), C10, C11 (`what's this $(4)$?`: "for" and "four" sound alike, and he explains the
notation $(4)$ right after, so no recording can settle it better than the context), and C15's line 816.

From Argon's own finds: W7 Wed:1184 (as `take the rotations of this cube`, not Argon's "this rotation group of the
cube is a group"), W9 Tue:1562, W7 Tue:307, W7 Tue:556, W7 Tue:1789, W8 Tue:1429, W7 Wed:317, W7 Wed:755, W10
Tue:757 (a comma, `play with, with the actions`, instead of Argon's "for"), and its Part II.B items 1–4, 6–11, 13–19
and 21. The WORD-SUSPECT comment at W10 Tue:492 became a WORD-CHECKED note citing W8 Tue (not heard).

Prompt side: the connector lists of Stages 1, 3 and 4 had `Okay, so,` since `a2ecbfd`; `All right, so,` followed in
`c3c31c0` (prompt-engineering).

### Not applied

- A9 (the speech box without speech): taste, and Argon's version rests on a sentence that does not exist.
- D1–D4: authentic; Argon agrees on D1 and D4.
- W1 Wed:1217 `(application?)`: stays, as its WORD-CHECKED comment decided after three hearings (Argon wanted
  `(i.e., application)`).
- Argon II.B.20 (W10 Wed:325, "the stabilizer" for $X$): he corrects himself in the same block, and the aiNote right
  after explains it.
- Argon C5 (W9 Tue:2463): already follows the slip convention.

### Settled by the audio (Gemini Neon, 2026-11-22)

The eight spots that needed the recording were cut as 27–44 s clips around each spot (ffmpeg, mono mp3), renamed
`clip1`–`clip8` so the file names gave nothing away, and transcribed word for word by Gemini 4 Neon XHigh through
`agy`, four clips per call, with no hint of the disputed words. One hearing each, so a settled word rests on Stage 1
and Neon agreeing; each changed block carries a `% [WORD-CHECKED (2026-11-22): ...]` comment.

| Spot | Book before | Neon heard | Result |
|---|---|---|---|
| W5 Wed:1025 (C9) | `something from the two side` | "the two-- the Z side and something from the two side" | spoken word kept, `(i.e., $x$)` added: the ideal is $(2, x)$ |
| W1 Wed:921 (C12) | `That's a wider property.` | "a-- a wider property" | kept |
| W9 Tue:219 (C16) | `it's a very good answer` | "it's a very good answer" | kept |
| W9 Tue:319 (C16) | `a hard question, not the answer, but` | "a hard question know the answer" | now `a hard question to know the answer, but` |
| W10 Wed:620 (C17) | `I'm just saying over what I've said already.` | "I've just saying over what I've said already" | kept |
| W10 Wed:866 (C17) | `because I don't have...` | "because we're [unclear]" | kept; three hearings, three versions (the rerun: "because you remember it") |
| W5 Wed:345 (Argon II.B.5) | `you pick where that you want` | "you pick where that you want" | spoken words kept, `(i.e., whatever you want)` added |
| W6 Tue:946 (Argon II.B.12) | `one at a time using if two` | "one at a time using, if you just, two" | kept, `(i.e., the case of two)` added |

Committed with the PDF rebuilt (745 pages, no errors, no undefined references).
