"""For each speech block of a book lecture, find its opening words in heard clips and estimate the time.
usage: blockstarts.py BOOK.tex CLIPROOT MODEL [FROM_hh:mm:ss TO_hh:mm:ss]
Clip files are named cNN-HHMMSS.mp3; each folder fK has out-MODEL.txt with '=== <name>' sections.
Estimate = clip start + 120 s * (word index / words in clip), so +-15 s."""
import re, sys, glob, os

sys.path.insert(0, os.path.dirname(__file__))
from cmp_speech import blocks, clean, norm_tokens  # noqa: E402  (cmp_speech guards main below)

book, root, model = sys.argv[1:4]
lo = hi = None
if len(sys.argv) > 5:
    f = lambda s: sum(int(x) * k for x, k in zip(s.split(':'), (3600, 60, 1)))
    lo, hi = f(sys.argv[4]), f(sys.argv[5])


def fmt(t):
    return f'{t // 3600:02d}:{t % 3600 // 60:02d}:{t % 60:02d}'


clips = []
for out in glob.glob(os.path.join(root, 'f*', f'out-{model}.txt')):
    txt = open(out, encoding='utf8').read()
    for m in re.finditer(r'^=== (c\d\d-(\d{6})\.mp3)\s*\n(.*?)(?=^=== c\d\d-|\Z)', txt, re.S | re.M):
        hh, mm, ss = int(m.group(2)[:2]), int(m.group(2)[2:4]), int(m.group(2)[4:])
        body = re.sub(r'\[(lecturer|student|unclear)\]', ' ', m.group(3))
        clips.append((hh * 3600 + mm * 60 + ss, m.group(1), norm_tokens(body)))
clips.sort()

for b in blocks(book):
    if b['kind'] != 'speech' or b['start'] is None:
        continue
    if lo is not None and not (lo - 60 <= b['start'] <= hi + 60):
        continue
    w = norm_tokens(clean(b['body']))
    found = None
    for n in (6, 5, 4):
        for off in range(0, 12):
            ph = w[off:off + n]
            if len(ph) < n:
                break
            for t0, name, cw in clips:
                for i in range(len(cw) - n + 1):
                    if cw[i:i + n] == ph:
                        found = (t0 + round(120 * i / len(cw)), name, ' '.join(ph), off)
                        break
                if found:
                    break
            if found:
                break
        if found:
            break
    if found:
        d = b['start'] - found[0]
        flag = '  <-- ' if abs(d) > 20 else ''
        print(f"line {b['line']:5d}  book {fmt(b['start'])}  heard ~{fmt(found[0])} ({found[1]}, '{found[2]}', word+{found[3]})  diff {d:+d}{flag}")
    else:
        print(f"line {b['line']:5d}  book {fmt(b['start'])}  (opening not found in clips)")
