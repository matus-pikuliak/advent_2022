vals = list(map(int, open('input')))
nexts = list(range(1, len(vals))) + [0]
prevs = [len(vals) - 1] + list(range(len(vals) - 1))

for i, val in enumerate(vals):
    if val == 0:
        continue
    p, n = prevs[i], nexts[i]
    nexts[p] = n
    prevs[n] = p
    val %= len(vals) - 1
    for _ in range(val):
        n = nexts[n]
    nexts[i] = n
    prevs[i] = prevs[n]
    nexts[prevs[n]] = i
    prevs[n] = i

out = 0
z = vals.index(0)
for x in range(3000):
    z = nexts[z]
    if x % 1000 == 999:
        out += vals[z]
print(out)
