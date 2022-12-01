elfs = [
    sum(map(int, group.split()))
    for group in open('input').read().split('\n\n')
]
print(max(elfs))
print(sum(sorted(elfs)[-3:]))

