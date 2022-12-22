points = {eval(f'({line})') for line in open('input').read().splitlines()}

visited, current = {(-1, -1, -1)}, {(-1, -1, -1)}


def n1(p):
    x, y, z = p
    return {
        np
        for np in ((x+1, y, z), (x-1, y, z), (x, y-1, z), (x, y+1, z), (x, y, z-1), (x, y, z+1))
        if np not in points and min(np) > -2 and max(np) < 21
    }


while current := set.union(*(n1(c) for c in current)) - visited:
    visited |= current


def n2(p):
    x, y, z = p
    return sum(
        np in visited
        for np in ((x+1, y, z), (x-1, y, z), (x, y-1, z), (x, y+1, z), (x, y, z-1), (x, y, z+1))
    )


print(
    sum(
        n2(p)
        for p in points
    )
)
