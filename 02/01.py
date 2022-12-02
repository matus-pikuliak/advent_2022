sw = {
    'A': 2, 'B': 1, 'C': 3,
    'X': 1, 'Y': 2, 'Z': 3,
}

codes = [(sw[line[0]], sw[line[2]]) for line in open('input').readlines()]
vals = [
    (
        b,
        (a + b) % 3 == 0,
        (a + b) == 4,
        (b - a + 1) % 3 or 3,
    )
    for a, b in codes
]

cols = list(map(sum, zip(*vals)))

print(cols[0] + 3 * cols[1] + 6 * cols[2])
print(cols[3] + 3 * cols[0] - 3 * len(vals))
