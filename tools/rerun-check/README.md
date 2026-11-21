# Checking a lecture against a pipeline rerun

Scripts used on 2026-11-15/16 to bring the Gemini Hydrogen XHIGH reruns into the
reviewed book (Weeks 1-6). The book stays the base; the rerun and heard audio
clips are witnesses. Run them with `py -3` from the repository root (Windows: the
`python` alias opens the Microsoft Store). In Git Bash, heredocs eat backslashes,
so keep regexes in files like these rather than inline.

## Workflow for one lecture

1. **Align the speech.**
   `py -3 tools/rerun-check/cmp_speech.py content/<book>.tex <rerun step4 .tex> out.md`
   Word-level diff of all `speech` and `student` blocks (board notes, `\cref`,
   `(Recall: ...)` and `(i.e., ...)` stripped; contractions, number words and
   fillers normalised). Lists only differences where a content word changes, and
   ends with a table of each book block's edges against the rerun's estimated
   time of the same words (`**` = off by more than 20 s at the start or 30 s at the end).
2. **Shortlist.** `py -3 tools/rerun-check/bigdiffs.py out.md 2` keeps the
   differences where at least two content words change: dropped clauses, slips,
   student lines. Most of the rest are wording variants that change nothing.
3. **Hear the disputed spots** (costs Gemini quota; ask first when it is low).
   Cut 120 s mp3 clips from the run folder's `*_audio.aac`
   (`ffmpeg -ss HH:MM:SS -t 120 -i audio.aac -ac 1 -ar 16000 -b:a 48k cNN-HHMMSS.mp3`),
   four per folder `f1`, `f2`, ..., then `bash tools/rerun-check/hear.sh <cliproot> <model>`
   (one `agy` call per folder, in parallel, skips folders already done). agy hands
   the model a ready-made caption of each clip, so Flash and Hydrogen hearings are
   not fully independent, and time marks are guesses: the script asks for none.
4. **Place words in time.**
   - `py -3 tools/rerun-check/blockstarts.py content/<book>.tex <cliproot> <model>`
     finds each block's first words in the heard clips and estimates their time
     from word position (good to about 15 s). Ignore matches far outside the clips:
     those are common phrases.
   - `py -3 tools/rerun-check/wordpos.py <out.txt> <clip.mp3> HH:MM:SS FROM TO "phrase" ...`
     does the same for single phrases, assuming even speech between FROM and TO
     seconds of the clip.
   - The recording's pauses settle edges best:
     `ffmpeg -i clip.mp3 -af silencedetect=noise=-32dB:d=2 -f null -`.
   - Re-time a block only where the rerun and the hearing (or the pauses) agree and
     differ from the book by more than 20 s; write a `% [TIMESTAMP-CORRECTED: ...]`
     comment with the old times. "Late" means the edge moves earlier.
5. **Edit**, following the book's conventions: a spoken slip stays as said with
   `(i.e., <meant word>)` and a `% [WORD-CHECKED: ...]` comment naming the witnesses;
   one header comment per lecture says what was checked.
6. **Check before building.**
   - `py -3 tools/rerun-check/timecheck.py content/<book>.tex` - block order, overlaps.
   - `py -3 tools/rerun-check/refcount.py HEAD: WT` - `\cref`, `\label`, `\recap`,
     `(Recall:` counts must not drop.
   - `py -3 tools/rerun-check/fwdrefs.py` - references from Weeks 1-6 into the
     group chapters; `showlabel.py 1 9 <label>` shows a label's box.
7. **Build, commit.** Build the PDF and commit it with the lecture. A Gemini
   review of the applied diff only when the user asks for one (the standing
   review rule was dropped on 2026-11-21: it costs tokens). To give each lecture its own commit with a matching PDF, build
   the intermediate states in copies of `git archive HEAD` with the lecture files
   overlaid.

See `findings/hydrogen-rerun-check.md` for the group chapters (Weeks 7-9), removed
from the tree on 2026-11-18 and kept in the history
(`git show 4d2b858:findings/hydrogen-rerun-check.md`), and the commit messages of
2026-11-15/16 for what each lecture's check found.
