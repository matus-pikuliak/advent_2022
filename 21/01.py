import re

lines = dict(line.split(': ') for line in open('input').read().splitlines())


# Part 1
s = lines['root']
while to_replace := re.findall(r'[a-z]{4}', s):
    for t in to_replace:
        s = s.replace(t, f'({lines[t]})')
print(eval(s))


# Part 2
lines['humn'] = 'X'
lines['root'] = lines['root'].replace('+', '-')
s = lines['root']
while to_replace := re.findall(r'[a-z]{4}', s):
    for t in to_replace:
        s = s.replace(t, f'({lines[t]})')

b = [0, 10**30]
while v := eval(s.replace('X', str(x := sum(b) // 2))):
    b[v < 0] = x
print(x)

