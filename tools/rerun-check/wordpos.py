"""Estimate when a phrase is spoken inside a heard clip, by word position.
usage: wordpos.py OUTFILE CLIPNAME CLIPSTART(hh:mm:ss) SPEECH_FROM_S SPEECH_TO_S "phrase" ["phrase" ...]
Assumes even speaking rate between SPEECH_FROM_S and SPEECH_TO_S (seconds into the clip)."""
import re, sys
out, clip, start, a, b = sys.argv[1:6]
h, m, s = map(int, start.split(':')); t0 = h * 3600 + m * 60 + s
a, b = float(a), float(b)
txt = open(out, encoding='utf8').read()
sec = txt.split('=== ' + clip)[1].split('\n===')[0]
sec = re.sub(r'\[(lecturer|student|unclear|\d\d:\d\d)\]', ' ', sec)
words = re.findall(r"[a-z0-9']+", sec.lower())
for ph in sys.argv[6:]:
    pw = re.findall(r"[a-z0-9']+", ph.lower())
    for i in range(len(words) - len(pw) + 1):
        if words[i:i + len(pw)] == pw:
            t = t0 + a + (b - a) * i / len(words)
            print(f'{ph!r}: word {i}/{len(words)} -> {int(t)//3600:02d}:{int(t)%3600//60:02d}:{int(t)%60:02d}')
            break
    else:
        print(f'{ph!r}: not found')
