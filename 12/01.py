from itertools import count

m = dict()

for i, line in enumerate(open('input').read().splitlines()):
    for j, c in enumerate(line):
        p = i + j * 1j
        if c == 'S':
            p1_start = p
            c = 'a'
        if c == 'E':
            cur = {p}
            c = 'z'
        m[p] = ord(c)


vis = set()
s = dict()

for i in count():
    for c in cur:
        s[c] = i
    cur = set(
        c + d
        for c in cur
        for d in [1, -1j, -1, 1j]
        if m.get(c + d, -200) - m[c] > -2
    ) - vis
    if not cur:
        break
    vis |= cur


print(s[p1_start])
print(
    min(
        s[p]
        for p, v in m.items()
        if v == ord('a') and p in s
    )
)

