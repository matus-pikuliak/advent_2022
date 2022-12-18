lines = open('input').readlines()

monkeys = [
    list(map(int, line.split(':')[1].split(',')))
    for line in lines[1::7]
]

inspect = [
    eval(f'lambda old: ({a}) // 3')
    for a in [line.split('=')[1] for line in lines[2::7]]
]

checks = [
    eval(f'lambda val: [{d}, {c}][val % {b} == 0]')
    for b, c, d in zip(
        [line.split()[-1] for line in lines[3::7]],
        [line.split()[-1] for line in lines[4::7]],
        [line.split()[-1] for line in lines[5::7]],
    )
]

counts = [0 for _ in range(len(monkeys))]

for _ in range(20):
    print(monkeys)
    for i in range(len(monkeys)):
        counts[i] += len(monkeys[i])
        while monkeys[i]:
            it = monkeys[i].pop(0)
            val = inspect[i](it)
            monkeys[checks[i](val)].append(val)

counts = sorted(counts)
print(counts[-1] * counts[-2])
