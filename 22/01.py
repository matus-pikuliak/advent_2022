import re

lines = open('input').read().splitlines()

#   0 1
#   2
# 3 4
# 5

box_coordinates = [(0, 1), (0, 2), (1, 1), (2, 0), (2, 1), (3, 0)]

boxes = [
    {
        i + j * 1j
        for i, line in enumerate(lines[row * 50:row * 50 + 50])
        for j, char in enumerate(line[col * 50:col * 50 + 50])
        if char == '#'
    }
    for row, col in box_coordinates
]

com_steps = map(int, re.findall(r'\d+', lines[-1]))
com_turns = iter(re.findall(r'[LR]', lines[-1]))

right = [1, 0, 2, 4, 3, 5]
left = [1, 0, 2, 4, 3, 5]
up = [4, 1, 0, 5, 2, 3]
down = [2, 1, 4, 5, 0, 3]

side, xy, rot = 0, 0, 1j

while True:
    for _ in range(next(com_steps)):

        new_xy = xy + rot
        new_side = side

        if new_xy.real == 50:
            new_xy = new_xy.imag * 1j
            new_side = down[side]
        elif new_xy.real == -1:
            new_xy = 49 + new_xy.imag * 1j
            new_side = up[side]
        elif new_xy.imag == 50:
            new_xy = new_xy.real
            new_side = right[side]
        elif new_xy.imag == -1:
            new_xy = new_xy.real + 49 * 1j
            new_side = left[side]

        if new_xy in boxes[new_side]:
            break

        xy = new_xy
        side = new_side

    try:
        rot *= {'L': 1j, 'R': -1j}[next(com_turns)]
    except StopIteration:
        r, c = [50 * x for x in box_coordinates[side]]
        r += 1 + int(xy.real)
        c += 1 + int(xy.imag)
        d = [1j, 1, -1j, -1].index(rot)
        print(1000 * r + 4 * c + d)
        break






