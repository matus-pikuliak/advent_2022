import re


def sign(a):
    return (a > 0) - (a < 0)


occupied = set()

for line in open('input'):
    coords = list(map(int, re.findall(r'\d+', line)))

    for c1, r1, c2, r2 in zip(*(coords[x::2] for x in range(4))):
        if c1 == c2:
            s = sign(r1 - r2)
            occupied |= {r + c1 * 1j for r in range(r1, r2 - s, -s)}
        else:
            s = sign(c1 - c2)
            occupied |= {r1 + c * 1j for c in range(c1, c2 - s, -s)}


stack = [500j]
lo = len(occupied)
max_r = max(o.real for o in occupied)

while stack[-1].real != max_r:
    c = stack[-1]
    nxt = next(
        (x for x in (c + 1, c + 1 - 1j, c + 1 + 1j) if x not in occupied),
        None
    )
    if not nxt:
        occupied.add(c)
        stack.pop()
    else:
        stack.append(nxt)

print(len(occupied) - lo)

stack = [500j]
while stack:
    c = stack[-1]
    nxt = next(
        (x for x in (c + 1, c + 1 - 1j, c + 1 + 1j) if x not in occupied and x.real < max_r + 2),
        None
    )
    if not nxt:
        occupied.add(c)
        stack.pop()
    else:
        stack.append(nxt)

print(len(occupied) - lo)

