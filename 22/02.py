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

down = [(2, 'U'), (2, 'R'), (4, 'U'), (5, 'U'), (5, 'R'), (1, 'U')]
up = [(5, 'L'), (5, 'D'), (0, 'D'), (2, 'L'), (2, 'D'), (3, 'D')]
right = [(1, 'L'), (4, 'Rx'), (1, 'D'), (4, 'L'), (1, 'Rx'), (4, 'D')]
left = [(3, 'Lx'), (0, 'R'), (3, 'U'), (0, 'Lx'), (3, 'R'), (0, 'U')]

side, xy, rot = 0, 0, 1j


def switch(val, dir):
    if 'x' in dir:
        val = 49 - val
        dir = dir[0]
    if dir == 'U':
        return val * 1j, 1
    if dir == 'D':
        return 49 + val * 1j, -1
    if dir == 'L':
        return val, 1j
    if dir == 'R':
        return val + 49 * 1j, -1j


while True:
    for _ in range(next(com_steps)):

        new_xy = xy + rot
        new_side = side
        new_rot = rot

        if new_xy.real == 50:
            new_xy, new_rot = switch(new_xy.imag, down[side][1])
            new_side = down[side][0]
        elif new_xy.real == -1:
            new_xy, new_rot = switch(new_xy.imag, up[side][1])
            new_side = up[side][0]
        elif new_xy.imag == 50:
            new_xy, new_rot = switch(new_xy.real, right[side][1])
            new_side = right[side][0]
        elif new_xy.imag == -1:
            new_xy, new_rot = switch(new_xy.real, left[side][1])
            new_side = left[side][0]

        if new_xy in boxes[new_side]:
            break

        xy = new_xy
        side = new_side
        rot = new_rot

    try:
        rot *= {'L': 1j, 'R': -1j}[next(com_turns)]
    except StopIteration:
        r, c = [50 * x for x in box_coordinates[side]]
        r += 1 + int(xy.real)
        c += 1 + int(xy.imag)
        d = [1j, 1, -1j, -1].index(rot)
        print(1000 * r + 4 * c + d)
        break





