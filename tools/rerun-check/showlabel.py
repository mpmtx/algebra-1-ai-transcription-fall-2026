"""Show the lines around \\label{...} for one or more labels in content/.

usage: py -3 tools/rerun-check/showlabel.py BEFORE AFTER label1 [label2 ...]
"""
import sys
from pathlib import Path

CONTENT = Path(__file__).resolve().parents[2] / 'content'
before, after = int(sys.argv[1]), int(sys.argv[2])
files = sorted(CONTENT.glob('step4-*.tex'))
for lab in sys.argv[3:]:
    key = '{' + lab + '}'
    for f in files:
        lines = f.read_text(encoding='utf8').split('\n')
        for i, l in enumerate(lines):
            if '\\label' in l and key in l:
                print(f'=== {lab}  ({f.name[11:45]}:{i + 1})')
                for x in lines[max(0, i - before):i + after + 1]:
                    print('   ', x[:330])
