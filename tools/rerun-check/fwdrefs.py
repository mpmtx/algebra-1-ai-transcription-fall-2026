"""List the cross-references from earlier lectures into later ones.

usage: py -3 tools/rerun-check/fwdrefs.py [--labels] [LATE_WEEK ...]
Default late weeks: week7 week8 week9 (the group chapters). Prints, per earlier
lecture, the \\cref targets that live in a late week; --labels also lists every
label of the late weeks.
"""
import re, sys
from pathlib import Path

CONTENT = Path(__file__).resolve().parents[2] / 'content'
LABEL = re.compile(r'\\label(?:\[[^\]]*\])?\{([^}]*)\}')
REF = re.compile(r'\\[cC]ref\{([^}]*)\}')

args = [a for a in sys.argv[1:] if not a.startswith('--')]
late_weeks = args or ['week7', 'week8', 'week9']
files = sorted(CONTENT.glob('step4-*.tex'))
lab = {}
for f in files:
    for m in LABEL.finditer(f.read_text(encoding='utf8')):
        lab[m.group(1)] = f
late = [f for f in files if any(w in f.name for w in late_weeks)]
early = [f for f in files if f not in late]
print('labels in', ', '.join(late_weeks) + ':', sum(1 for v in lab.values() if v in late))
for f in early:
    refs = [r.strip() for g in REF.findall(f.read_text(encoding='utf8')) for r in g.split(',')]
    fw = [r for r in refs if lab.get(r) in late]
    print(f.name[11:40], 'forward refs:', fw)
if '--labels' in sys.argv:
    for k, v in lab.items():
        if v in late:
            print(v.name[11:40], k)
