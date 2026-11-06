# Open items from the final review

The final review of the lecture notes (12–13 October 2026) fixed what it found in commit `fd085cf`, except three spots that can only be settled against the lecture recordings, which are not on this computer. Each one needs a few seconds of audio; item 3 also needs the video. A second review (23 October 2026) added item 4, and a review on 5 November 2026 item 6. Items 1 and 5 are settled and removed; the numbers of the others are unchanged.

None of these recordings is complete on this computer now. `D:\Download backup\Downloads\Algebra_I\Nicht bestätigt 441694.crdownload` is the 22 September recording, but it stops at about 01:15, before item 2. The file `10-14-2026-wednesday-week5-Algebra_I-speed-1-compressed.mp4` in `D:\Download backup\Downloads\Algebra_I\` is the book's 10-15 Wednesday lecture, not the 10-14 Tuesday lecture of items 4 and 6.

When an item is settled, fix it, rebuild `algebra-1.pdf`, and delete the item from this file (or the whole file, once all are done).

## 2. Week 2 Tuesday: "there's a motion giving a vector space another one"

- **Where:** [`content/step4-2026-09-22-tuesday-week2-algebra-1-offset-final.tex`, line 2408](content/step4-2026-09-22-tuesday-week2-algebra-1-offset-final.tex#L2408), in the speech block `[01:30:08 - 01:30:50]` (line 2403).
- **Current text:** "I'm just saying there's a motion giving a vector space another one, and that's the double dual, and it's functorial in this sense."
- **Suspected:** "there's a **notion** giving a vector space another one". "Motion" makes no sense here.
- **Check:** recording `2026-09-22-tuesday-week2-algebra-1.mp4`, 01:30:08–01:30:50.
- **Fix if confirmed:** replace `motion` with `notion`.

## 3. Week 4 Wednesday: two speech blocks overlap by 10 seconds

- **Where:** [`content/step4-2026-10-07-wednesday-week4-algebra-1-offset-final.tex`, lines 216 and 240–241](content/step4-2026-10-07-wednesday-week4-algebra-1-offset-final.tex#L240).
- **Problem:** the block at line 216 is `[00:07:05 - 00:08:15]`, but the next block (line 241) starts at `00:08:05`. Line 240 still carries the pipeline's marker `% [TIMESTAMP-SUSPECT: inspect manually — original: 00:08:05 - 00:10:25]`.
- **Check:** in the 7 October recording, find where "…that's the main thing this week." ends and "So, we'll explore (ii) a bit more today." begins. Shortly after, the lecturer writes "Let f: R → S be any hom. of rings" on the board. This file's pipeline header names the run `2026-10-07-wednesday-week3-algebra-1`, so the recording may carry that name rather than `week4`.
- **Fix:** set the end of the first block and the start of the second to that time. Replace the marker on line 240 with a `% [TIMESTAMP-CORRECTED: …]` comment saying what the recording showed, as the other lecture files do.

## 4. Week 5 Tuesday: two speech blocks overlap by 16 seconds

- **Where:** [`content/step4-2026-10-14-tuesday-week5-algebra-1-offset-final.tex`, lines 1412 and 1420](content/step4-2026-10-14-tuesday-week5-algebra-1-offset-final.tex#L1420).
- **Problem:** the block at line 1412 is `[01:04:41 - 01:05:40]`, but the next block (line 1420) starts at `01:05:24`. The text does not repeat across the boundary, so one of the two times is simply off. `01:05:24` is exactly where pipeline Part 4 starts, so it is probably the suspect one.
- **Check:** in the 14 October recording, find where "…Anyway, we can now ask: Is this a prime ideal?" ends and "And the answer is no." begins.
- **Fix:** set the end of the first block and the start of the second to that time, with a `% [TIMESTAMP-CORRECTED: …]` comment.
- **Not worth an item:** the same file has a 1-second overlap at line 1040 (`00:46:53` / `00:46:52`), which is rounding.

## 6. Week 5 Tuesday: two more split speech blocks with estimated times

- **Where:** [`content/step4-2026-10-14-tuesday-week5-algebra-1-offset-final.tex`, lines 719–729 and 1241–1260](content/step4-2026-10-14-tuesday-week5-algebra-1-offset-final.tex#L719).
- **Problem:** the pipeline split two speech blocks around student remarks and estimated the split times without the audio: `00:31:18 - 00:32:23` around "Transitivity." (`00:31:22`/`00:31:24`), and `00:57:40 - 00:58:06` around the student's two remarks (`00:57:45`/`00:57:47` and `00:57:48`/`00:57:50`). Each block is marked `% [TIMESTAMP-SUSPECT: estimated without audio …]`.
- **Check:** in the 14 October recording, find where the student says "Transitivity.", "What if $R$ is a field?" and "Then the prime ideal...".
- **Fix:** set the block boundaries to those times and replace each marker with a `% [TIMESTAMP-CORRECTED: …]` comment.
