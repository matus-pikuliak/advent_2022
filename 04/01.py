nums = [
    map(int, line.strip().replace(',', '-').split('-'))
    for line in open('input')
]
ranges = [
    (set(range(a, b + 1)), set(range(c, d + 1)))
    for a, b, c, d in nums
]

print(
    sum(
        not bool(a - b and b - a)
        for a, b in ranges
    )
)

print(
    sum(
        bool(a & b)
        for a, b in ranges
    )
)
