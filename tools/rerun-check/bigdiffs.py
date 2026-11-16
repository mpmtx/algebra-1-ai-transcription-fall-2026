"""List differences from a speech-diff.md where at least N content words change.  usage: bigdiffs.py FILE [N]"""
import re, sys
from collections import Counter
FUN = set('''is are was were be been it its they them this that these those there here we you your i me my he she s ll d ve re
will would shall should had have has do does did of in on at to for with as by from into but or if then than also too very so
just which who what where when how can could may might an then thing things get got going gonna let us our um uh er ah okay ok
right yeah well like actually basically know mean kind sort all alright now oh hmm and the a mod'''.split())
N = int(sys.argv[2]) if len(sys.argv) > 2 else 2
t = open(sys.argv[1], encoding='utf8').read()
for m in re.finditer(r'## (D\d+)\s+book (\S+) \(line (\d+)\)\s+rerun (\S+) \(line (\d+)\)\n\s+(.*)', t):
    s = m.group(6)
    b = re.search(r'\[\[BOOK: (.*?)\]\]', s).group(1).split()
    r = re.search(r'\[\[RERUN: (.*?)\]\]', s).group(1).split()
    cb = Counter(w for w in b if w not in FUN); cr = Counter(w for w in r if w not in FUN)
    if sum(((cb - cr) + (cr - cb)).values()) >= N:
        print(m.group(1), m.group(2), 'L' + m.group(3), '|', re.sub(r'^\.\.\.', '', s)[:250])
