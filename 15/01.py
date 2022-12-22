import re

sensors = [
    list(map(int, re.findall(r'\d+', line)))
    for line in open('input')
]


def intersect(sensor, row):
    x, y, x_b, y_b = sensor
    size = abs(x - x_b) + abs(y - y_b)
    if abs(y - row) <= size:
        dlt = size - abs(y - row)
        return x - dlt, x + dlt


def intersects(sensors, row):
    slices = sorted(filter(None, (intersect(s, row) for s in sensors)))
    while len(slices) > 1 and slices[0][1] >= slices[1][0]:
        n = slices[0][0], max(slices[0][1], slices[1][1])
        slices.pop(0)
        slices[0] = n
    return slices

# Part 1
j = intersects(sensors, 2_000_000)[0]
print(j[1] - j[0])  # +1 diff, -1 existing beacon cancel out

# Part 2
for y_tgt in range(4_000_000):
    ints = intersects(sensors, y_tgt)
    if len(ints) > 1:
        x = ints[0][1] + 1
        print(y_tgt + x * 4_000_000)
        break