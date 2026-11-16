"""Count cross-references in content/ for two git specs, e.g. refcount.py HEAD: :   (':' = index, 'WT' = working tree)."""
import subprocess, re, sys

PATS = {'cref': r'\\[cC]ref\{', 'label': r'\\label', 'recap': r'\\recap\{', 'Recall': r'\(Recall:'}


def text(spec, f):
    if spec == 'WT':
        return open(f, encoding='utf8').read()
    return subprocess.run(['git', 'show', spec + f], capture_output=True, text=True, encoding='utf8').stdout


files = subprocess.run(['git', 'ls-files', 'content'], capture_output=True, text=True).stdout.split()
for spec in sys.argv[1:]:
    tot = {k: 0 for k in PATS}
    for f in files:
        t = text(spec, f)
        for k, p in PATS.items():
            tot[k] += len(re.findall(p, t))
    print(f'{spec:5s}', tot)
