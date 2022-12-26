from itertools import count

borders = set()
winds = dict()
wind_dirs = {'>': 1j, '<': -1j, '^': -1, 'v': 1}
for i, line in enumerate(open('input')):
    for j, char in enumerate(line.strip()):
        pos = i + j * 1j - 1 - 1j
        if char == '#':
            borders.add(pos)
        if char in wind_dirs:
            winds[pos] = wind_dirs[char]
borders |= {-2, pos + 1 - 1j}
width = pos.imag
height = pos.real


def mod_complex(x, mod_r, mod_i):
    return x.real % mod_r + x.imag % mod_i * 1j


start_pos = {-1}
end_pos = {height + (width - 1) * 1j}

positions, target = set(start_pos), set(end_pos)
s = 0
for i in count():
    positions = {
        pos + d
        for pos in positions
        for d in [-1,0,1,-1j,1j]
        if pos + d not in borders
    } - {
        mod_complex(pos + i * dir, height, width)
        for pos, dir in winds.items()
    }
    if target & positions:
        if s == 0:
            print('Part 1:', i)
            positions, target = set(end_pos), set(start_pos)
        if s == 1:
            positions, target = set(start_pos), set(end_pos)
        if s == 2:
            print('Part 2:', i)
            break
        s += 1



