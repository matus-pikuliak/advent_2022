path = ''.join(c * int(s) for c, s in [line.split() for line in open('input').readlines()])

h = [0 + 0j]
t = [0 + 0j]
dirs = {c: -1j**i for i, c in enumerate('ULDR')}

for step in path:
    h.append(h[-1] + dirs[step])
    df = h[-1] - t[-1]
    if {-2, 2} & {df.real, df.imag}:
        t.append(h[-2])

print(len(set(t)))
