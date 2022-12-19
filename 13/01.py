from functools import cmp_to_key


def sign(a):
    return (a > 0) - (a < 0)


def compare(al, bl):
    for a, b in zip(al, bl):
        try:
            if s := sign(a - b):
                return s
        except TypeError:
            if isinstance(a, int):
                a = [a]
            if isinstance(b, int):
                b = [b]
            if o := compare(a, b):
                return o

    if s := sign(len(al) - len(bl)):
        return s


lines = open('input').read().splitlines()
lines_1 = list(map(eval, lines[0::3]))
lines_2 = list(map(eval, lines[1::3]))
div_1 = [[2]]
div_2 = [[6]]

print(
    sum(
        i + 1
        for i, (l1, l2) in enumerate(zip(lines_1, lines_2))
        if compare(l1, l2) == -1
    )
)

srt = sorted(lines_1 + lines_2 + [div_1, div_2], key=cmp_to_key(compare))
print((srt.index(div_1) + 1) * (srt.index(div_2) + 1))