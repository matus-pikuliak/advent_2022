from collections import Counter
from itertools import chain, count

elfs = {
    i + 1j * j
    for i, line in enumerate(open('input'))
    for j, char in enumerate(line)
    if char == '#'
}


def new_pos(i, elf):
    groups = [
        [-1-1j, -1, -1+1j],
        [1-1j, 1, 1+1j],
        [-1-1j, -1j, 1-1j],
        [-1+1j, 1j, 1+1j],
    ]
    if elfs & {elf + n for n in chain.from_iterable(groups)}:
        for j in range(4):
            group = groups[(i + j) % 4]
            if not {elf + n for n in group} & elfs:
                return elf + group[1]


for i in count():
    new_elfs = {
        elf: new_pos(i, elf)
        for elf in elfs
    }

    valid = {
        pos
        for pos, count in Counter(new_elfs.values()).items()
        if count == 1 and pos is not None
    }

    if elfs == (elfs := {
        new_elfs[elf] if new_elfs[elf] in valid else elf
        for elf in elfs
    }):
        print('Part 2:', i + 1)
        break

    if i == 9:
        reals = [elf.real for elf in elfs]
        imags = [elf.imag for elf in elfs]
        rd = max(reals) - min(reals) + 1
        ri = max(imags) - min(imags) + 1
        print('Part 1:', int(rd * ri - len(elfs)))
