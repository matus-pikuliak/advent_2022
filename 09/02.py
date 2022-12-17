path = ''.join(c * int(s) for c, s in [line.split() for line in open('input').readlines()])

r = [[0 + 0j] for _ in range(10)]
dirs = {c: -1j**i for i, c in enumerate('ULDR')}


def sign(n):
    return (n > 0) - (n < 0)


for step in path:
    r[0].append(r[0][-1] + dirs[step])
    for h, t in zip(r, r[1:]):
        df = h[-1] - t[-1]
        if {-2, 2} & {df.real, df.imag}:
            t.append(t[-1] + sign(df.real) + sign(df.imag) * 1j)

print(len(set(r[-1])))
