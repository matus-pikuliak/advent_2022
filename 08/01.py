from itertools import takewhile
from math import prod
from operator import truth

MAX = 99

m = {
    (i, j): int(ch)
    for i, line in enumerate(open('input').read().splitlines())
    for j, ch in enumerate(line)
}


def visible(x, y):
    return any(map(all,
        [
            (m[i, y] < m[x, y] for i in range(x)),
            (m[i, y] < m[x, y] for i in range(x + 1, MAX)),
            (m[x, i] < m[x, y] for i in range(y)),
            (m[x, i] < m[x, y] for i in range(y + 1, MAX)),
        ]
    ))


def scenic(x, y):
    return prod(
        map(
            lambda l: (o := sum(takewhile(truth, (v < m[x, y] for v in l)))) + (o != len(l)),
            [
                [m[i, y] for i in range(x - 1, -1, -1)],
                [m[i, y] for i in range(x + 1, MAX)],
                [m[x, i] for i in range(y - 1, -1, -1)],
                [m[x, i] for i in range(y + 1, MAX)],
            ]
        )
    )


print(sum(visible(x, y) for x in range(MAX) for y in range(MAX)))
print(max(scenic(x, y) for x in range(MAX) for y in range(MAX)))
