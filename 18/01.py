points = {eval(f'({line})') for line in open('input').read().splitlines()}


def n(p):
    x, y, z = p
    return sum(
        np in points
        for np in ((x+1, y, z), (x-1, y, z), (x, y-1, z), (x, y+1, z), (x, y, z-1), (x, y, z+1))
    )


print(
    sum(
        6 - n(p)
        for p in points
    )
)

