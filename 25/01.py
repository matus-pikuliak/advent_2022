def dec_to_snafu(num, base=5):
    out = ""
    while num != 0:
        rest = (num % base + 2) % base - 2
        out = {-2: "=", -1: "-"}.get(rest, str(rest)) + out
        num = (num - rest) // base
    return out


def snafu_to_dec(num):
    out = 0
    for i, c in enumerate(reversed(num)):
        val = "=-012".index(c) - 2
        out += 5**i * val
    return out


print(
    dec_to_snafu(
        sum(
            map(snafu_to_dec, open("input").read().splitlines())
        )
    )
)