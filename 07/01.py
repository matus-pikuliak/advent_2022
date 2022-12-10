import re
lines = open('input').read().splitlines()
cd_lines = [i for i, line in enumerate(lines) if re.match(r'\$ cd (?!\.)', line)]


def size(i):
    check, acc = 0, 0
    for x in range(i, len(lines)):
        line = lines[x]
        if line.startswith('$ cd'):
            check -= 1 - 2 * (x in cd_lines)
            if check <= 0:
                return acc
        if line[0].isdigit():
            acc += int(line.split()[0])
    return acc


print(
    sum(
        size(i)
        for i in cd_lines
        if size(i) <= 100000
    )
)

print(
    min(
        size(i)
        for i in cd_lines
        if size(i) >= size(0) - 40_000_000
    )
)