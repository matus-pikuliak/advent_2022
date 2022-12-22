from itertools import cycle

directions = cycle(open('input').read())
shapes = cycle([
    {0, 1j, 2j, 3j},
    {1, 1j, 1 + 1j, 2 + 1j, 1 + 2j},
    {0, 1j, 2j, 1 + 2j, 2 + 2j},
    {0, 1, 2, 3},
    {0, 1j, 1, 1 + 1j},
])

full = {-1 + i * 1j for i in range(7)}
difs = []
for step in range(2022):
    max_r = max(i.real for i in full)
    shape = {s + max_r + 4 + 2j for s in next(shapes)}
    mov = cycle([True, False])
    while True:
        if next(mov):
            lr = {'>': 1j, '<': -1j}[next(directions)]
            new_shape = {s + lr for s in shape}
            if 0 <= min(s.imag for s in new_shape) and 6 >= max(s.imag for s in new_shape) and not (new_shape & full):
                shape = new_shape
        else:
            new_shape = {s - 1 for s in shape}
            if new_shape & full:
                full |= shape
                df = max(s.real for s in shape) - max_r
                if df == -40:
                    print(step, int(max_r))
                break
            else:
                shape = new_shape

print(int(max(i.real for i in full) + 1))

# Part 2
# I observed the biggest drops of shape and observed that -40 seems to be the biggest drop
# I printed step and tower size when this happens and obtained following data:

# 1448 2253
# 3178 4912
# 4908 7571
# 6638 10230
# 8368 12889

# From this I observed that there is an initialization epoch with 1448 steps that results in 2253 tall tower
# All the subsequent epochs are similar: tower grows by 2659 steps in 1730 steps

# From this we can calculate the results easily:
#   (1) We can calculate number of steps in the repeating pattern by:
#          (1000000000000 - 1448) % 1730 = 422
#          (total number of steps - initialization steps) % number of steps per epoch
#   (2) We can calculate the size everywhere aside from the repeating pattern by using the script to calculate the
#       size of the tower after (1446 + 422) steps. That is the initialization pattern and the stub on the top. This
#       is equal to 2890
#   (3) We can finally calculate the final size by:
#          2890 + 2659 * ((1000000000000 - 1448) // 1730) = 1536994219669
#          size of stubs from (2) + size of repeating pattern * (number of repetitions)
