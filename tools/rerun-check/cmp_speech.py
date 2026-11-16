"""Align the speech of a book lecture with a rerun of it, word by word.

usage: py -3 cmp_speech.py BOOK.tex RERUN.tex OUT.md
Prints (to OUT.md) every difference that is not made only of fillers, with the
book's and the rerun's block times, plus a table of block-time disagreements.
"""
import re, sys, difflib

FILLERS = set('''um uh er ah so okay ok right yeah well like actually basically
you know i mean kind of sort just all alright now oh hmm and the a'''.split())


def strip_braced(text, cmd):
    """Remove \\cmd{...} with nested braces (and an optional [..] before)."""
    out, i = [], 0
    pat = re.compile(r'\\' + cmd + r'\*?(\[[^\]]*\])?\{')
    while True:
        m = pat.search(text, i)
        if not m:
            out.append(text[i:]); break
        out.append(text[i:m.start()])
        depth, j = 1, m.end()
        while j < len(text) and depth:
            if text[j] == '{': depth += 1
            elif text[j] == '}': depth -= 1
            j += 1
        out.append(' ')
        i = j
    return ''.join(out)


def keep_braced(text, cmd):
    """Replace \\cmd{X} by X (nested braces ok)."""
    pat = re.compile(r'\\' + cmd + r'\{')
    while True:
        m = pat.search(text)
        if not m: return text
        depth, j = 1, m.end()
        while j < len(text) and depth:
            if text[j] == '{': depth += 1
            elif text[j] == '}': depth -= 1
            j += 1
        text = text[:m.start()] + text[m.end():j - 1] + text[j:]


def ts(s):
    h, m, x = s.split(':')
    return int(h) * 3600 + int(m) * 60 + int(x)


def fmt(t):
    return f'{t // 3600:02d}:{t % 3600 // 60:02d}:{t % 60:02d}' if t is not None else '--:--:--'


BLOCK = re.compile(r'\\begin\{(speech|student)\}(?:\[([^\]]*)\])?(.*?)\\end\{\1\}', re.S)


def blocks(path):
    t = open(path, encoding='utf8').read()
    res = []
    for m in BLOCK.finditer(t):
        kind, opt, body = m.group(1), m.group(2) or '', m.group(3)
        tm = re.match(r'\s*(\d+:\d+:\d+)\s*-\s*(\d+:\d+:\d+)', opt)
        start, end = (ts(tm.group(1)), ts(tm.group(2))) if tm else (None, None)
        line = t.count('\n', 0, m.start()) + 1
        res.append(dict(kind=kind, start=start, end=end, body=body, line=line))
    return res


def clean(body):
    b = re.sub(r'(?m)%.*$', ' ', body)
    for c in ('inlinemetanote', 'cref', 'Cref', 'label', 'eqref'):
        b = strip_braced(b, c)
    b = re.sub(r'\(Recall:[^()]*(\([^()]*\)[^()]*)*\)', ' ', b)
    b = re.sub(r'\(i\.e\.,[^()]*(\([^()]*\)[^()]*)*\)', ' ', b)
    for c in ('qt', 'emph', 'textbf', 'text', 'textit', 'newterm', 'mathrm', 'operatorname'):
        b = keep_braced(b, c)
    b = b.replace('---', ' ').replace('--', ' ').replace('~', ' ')
    return b


def norm_tokens(text):
    t = text.lower()
    t = t.replace("’", "'")
    reps = [("it's", 'it is'), ("that's", 'that is'), ("there's", 'there is'), ("what's", 'what is'),
            ("let's", 'let us'), ("don't", 'do not'), ("doesn't", 'does not'), ("isn't", 'is not'),
            ("can't", 'cannot'), ("won't", 'will not'), ("i'm", 'i am'), ("you're", 'you are'),
            ("we're", 'we are'), ("they're", 'they are'), ("i'll", 'i will'), ("we'll", 'we will'),
            ("you'll", 'you will'), ("i've", 'i have'), ("we've", 'we have'), ("you've", 'you have'),
            ("here's", 'here is'), ("he's", 'he is'), ("didn't", 'did not'), ("aren't", 'are not'),
            ("wasn't", 'was not'), ("haven't", 'have not'), ("shouldn't", 'should not'), ("wouldn't", 'would not'),
            ("couldn't", 'could not'), ("i'd", 'i would'), ("you'd", 'you would'), ("we'd", 'we would'),
            ('is equal to', 'equals'), ('is equal', 'equals'), ('all right', 'alright')]
    for a, b in reps:
        t = t.replace(a, b)
    t = re.sub(r'\\[a-z]+', lambda m: ' ' + m.group(0)[1:] + ' ', t)
    t = re.sub(r'[^a-z0-9+\-=<>]+', ' ', t)
    t = re.sub(r'([+\-=<>])', r' \1 ', t)
    words = {'zero': '0', 'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6',
             'seven': '7', 'eight': '8', 'nine': '9', 'ten': '10', 'bmod': 'mod', 'pmod': 'mod',
             'equal': 'equals', 'minus': '-', 'plus': '+', 'ii': '2', 'iii': '3', 'times': 'cdot'}
    drop = {'faktor', 'mathbb', 'mathcal', 'mathfrak', 'cdot', 'dots', 'ldots', 'cdots', 'left', 'right',
            'bigl', 'bigr', 'big', 'quad', 'qquad', 'colon', 'hat', 'bar', 'overline', 'tilde', 'frac',
            'binom', 'choose', 'to', 'the', 'of', 'mathbf'}
    out = []
    for w in t.split():
        w = words.get(w, w)
        if w in drop:
            continue
        out.append(w)
    return out


FUNCTION = set('''is are was were be been being it its they them their this that these those there here we
you your i me my he she s ll d ve re will would shall should had have has do does did of in on at to for with
as by from into but or if then than also too very so just which who what where when how can could may might
an there's then thing things get got going gonna let us our'''.split())


def content_words(ws):
    return sorted(w for w in ws if w not in FILLERS and w not in FUNCTION)


def tokens_of(blks):
    toks, owner = [], []
    for k, b in enumerate(blks):
        w = norm_tokens(clean(b['body']))
        if b['kind'] == 'student':
            w = ['<student>'] + w + ['</student>']
        toks += w
        owner += [k] * len(w)
    return toks, owner


def raw_window(blk, words):
    return ' '.join(words)


def main():
    book, rerun, out = sys.argv[1], sys.argv[2], sys.argv[3]
    B, R = blocks(book), blocks(rerun)
    bt, bo = tokens_of(B)
    rt, ro = tokens_of(R)
    sm = difflib.SequenceMatcher(None, bt, rt, autojunk=False)
    lines = []
    same = sum(bl.size for bl in sm.get_matching_blocks())
    lines.append(f'# Speech comparison\n\nbook: {book}\nrerun: {rerun}\n')
    lines.append(f'book words {len(bt)}, rerun words {len(rt)}, matched {same} ({100*same/max(1,len(bt)):.1f}% of book)\n')
    n = 0
    for op, i1, i2, j1, j2 in sm.get_opcodes():
        if op == 'equal':
            continue
        a, b = bt[i1:i2], rt[j1:j2]
        if all(x in FILLERS for x in a + b):
            continue
        if content_words(a) == content_words(b):
            continue
        n += 1
        bk = B[bo[min(i1, len(bo) - 1)]]
        rk = R[ro[min(j1, len(ro) - 1)]]
        ctx_l = ' '.join(bt[max(0, i1 - 8):i1])
        ctx_r = ' '.join(bt[i2:i2 + 8])
        lines.append(f'## D{n}  book {fmt(bk["start"])} (line {bk["line"]})  rerun {fmt(rk["start"])} (line {rk["line"]})')
        lines.append(f'    ...{ctx_l} [[BOOK: {" ".join(a)}]] [[RERUN: {" ".join(b)}]] {ctx_r}...\n')
    # block-time comparison: for each book block, where do its first and last matched words land in the rerun?
    bmap = {}
    for bl in sm.get_matching_blocks():
        for k in range(bl.size):
            bmap[bl.a + k] = bl.b + k
    # estimated time of every rerun token: block start + position share of the block's duration
    rtime = [None] * len(rt)
    for k, r in enumerate(R):
        idx = [i for i in range(len(ro)) if ro[i] == k]
        if not idx or r['start'] is None:
            continue
        for p, i in enumerate(idx):
            rtime[i] = r['start'] + round(p / len(idx) * (r['end'] - r['start']))
    lines.append('\n# Block times (book block edges vs. estimated rerun time of its first/last matched word)\n')
    lines.append('| book line | book time | rerun est. first word | rerun est. last word | start diff | end diff |')
    lines.append('|---|---|---|---|---|---|')
    for k, b in enumerate(B):
        if b['kind'] != 'speech':
            continue
        idx = [i for i in range(len(bo)) if bo[i] == k]
        mi = [bmap[i] for i in idx if i in bmap]
        if not mi or b['start'] is None:
            lines.append(f'| {b["line"]} | {fmt(b["start"])}-{fmt(b["end"])} | (no match) | | | |')
            continue
        t1, t2 = rtime[mi[0]], rtime[mi[-1]]
        d1 = b['start'] - t1 if t1 is not None else None
        d2 = b['end'] - t2 if t2 is not None else None
        flag = ' **' if (d1 is not None and abs(d1) > 20) or (d2 is not None and abs(d2) > 30) else ''
        lines.append(f'| {b["line"]} | {fmt(b["start"])}-{fmt(b["end"])} | {fmt(t1)} | {fmt(t2)} | {d1} | {d2}{flag} |')
    open(out, 'w', encoding='utf8').write('\n'.join(lines))
    print(f'{n} differences; book words {len(bt)}, rerun {len(rt)}, matched {100*same/max(1,len(bt)):.1f}%')


if __name__ == "__main__":
    main()
