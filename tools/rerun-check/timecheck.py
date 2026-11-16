import re, sys
for p in sys.argv[1:]:
    t = open(p, encoding='utf8').read()
    prev_end, prev_line = None, None
    bad = 0
    for m in re.finditer(r'\\begin\{speech\}\[(\d+):(\d+):(\d+) - (\d+):(\d+):(\d+)\]', t):
        a = int(m.group(1)) * 3600 + int(m.group(2)) * 60 + int(m.group(3))
        b = int(m.group(4)) * 3600 + int(m.group(5)) * 60 + int(m.group(6))
        line = t.count('\n', 0, m.start()) + 1
        if b <= a:
            print(f'{p[-50:]}: line {line} ends before it starts'); bad += 1
        if prev_end is not None and a < prev_end:
            print(f'{p[-50:]}: line {line} starts {a - prev_end:+d} s before the previous block (line {prev_line}) ends'); bad += 1
        prev_end, prev_line = b, line
    print(p[-50:], 'ok' if not bad else f'{bad} problems')
