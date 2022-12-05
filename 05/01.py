import re
import copy


lines = open('input').readlines()

stacks = zip(*[line.ljust(36, ' ')[1::4] for line in lines[:8]])
stacks = [[crate for crate in reversed(stack) if crate != ' '] for stack in stacks]
stacks.extend(copy.deepcopy(stacks))

for line in lines[10:]:
    a, b, c = map(int, re.findall(r'\d+', line))

    b -= 1; c -= 1
    for _ in range(a):
        stacks[c].append(stacks[b].pop())

    b += 9; c += 9
    stacks[c].extend(stacks[b][-a:])
    stacks[b] = stacks[b][:-a]

out = ''.join(s[-1] for s in stacks)
print(out[:9], out[9:])
