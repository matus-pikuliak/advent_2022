def vm():
    reg = 1
    for line in open('input').readlines():
        match line.split():
            case ['addx', num]:
                yield reg
                yield reg
                reg += int(num)
            case ['noop']:
                yield reg


l = list(vm())
print(sum((x + 1) * l[x] for x in range(19, 220, 40)))

g = vm()
for _ in range(6):
    for i in range(40):
        if abs(next(g) - i) < 2:
            print('#', end='')
        else:
            print('.', end='')
    print()

