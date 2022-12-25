import re

lines = dict(line.split(': ') for line in open('input').read().splitlines())
s = lines['root']
while to_replace := re.findall(r'[a-z]{4}', s):
    for t in to_replace:
        s = s.replace(t, f'({lines[t]})')
print(eval(s))

lines['humn'] = 'X'
lines['root'] = lines['root'].replace('+', '-')
s = lines['root']
while to_replace := re.findall(r'[a-z]{4}', s):
    for t in to_replace:
        s = s.replace(t, f'({lines[t]})')


l = 0
h = 10**30
while True:
    x = (l + h) // 2
    v = eval(s.replace('X', str(x)))
    if v == 0:
        print(x)
        break
    if v > 0:
        l = x
    if v < 0:
        h = x
