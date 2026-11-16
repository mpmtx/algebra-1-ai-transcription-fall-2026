#!/bin/bash
# usage: hear.sh CLIPROOT MODEL   -- one agy call per subfolder f*, in parallel; skips folders with a complete out.txt
# MODEL e.g. gemini-3.8-flash-high or gemini-4-hydrogen-xhigh; both cost weekly quota, so it is not defaulted.
ROOT="$1"; MODEL="$2"
[ -n "$ROOT" ] && [ -n "$MODEL" ] || { echo "usage: hear.sh CLIPROOT MODEL" >&2; exit 2; }
AGY="C:/Users/miche/AppData/Local/agy/bin/agy.exe"
for d in "$ROOT"/f*/; do
  n=$(ls "$d"*.mp3 2>/dev/null | wc -l)
  if [ -f "$d/out-$MODEL.txt" ] && [ "$(grep -c '^===' "$d/out-$MODEL.txt")" -ge "$n" ]; then continue; fi
  files=$(cd "$d" && ls *.mp3 | tr '\n' ' ')
  (
    cd "$d" && "$AGY" --model "$MODEL" --mode plan --print-timeout 900s -p "Answer directly in this reply. Do not make a plan, do not create or edit files, do not run commands, do not ask questions.
The current folder contains these audio files (lecture recordings, a university algebra course): $files
Transcribe each file completely and word for word, including false starts, repetitions and fillers (um, uh, so, okay). Mark who speaks: [lecturer] or [student]. Write [unclear] for words you cannot make out. Start a new line for every sentence; do not add time marks. Mathematical expressions as spoken, in words.
Output format, for every file in the order listed:
=== <filename>
<transcript>" > "out-$MODEL.txt" 2>&1
  ) &
done
wait
for d in "$ROOT"/f*/; do echo "$d: $(grep -c '^===' "$d/out-$MODEL.txt" 2>/dev/null) of $(ls "$d"*.mp3 | wc -l)"; done
