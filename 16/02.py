import re
from itertools import chain, product, combinations

neigh = dict()
nodes = dict()
for line in open('input'):
    codes = re.findall(r'[A-Z]{2}', line)
    neigh[codes[0]] = set(codes[1:])
    rate = int(re.findall(r'\d+', line)[0])
    if rate > 0:
        nodes[codes[0]] = rate

nodes_ids = {node: i for i, node in enumerate(nodes)}


steps = dict()
for start in list(nodes) + ['AA']:
    visited, current = {start}, {start}
    i = 0
    while current := set.union(*(neigh[node] for node in current)) - visited:
        i += 1
        for node in current & set(nodes):
            steps[start, node] = i
        visited |= current

states = [dict() for _ in range(27)]
states[0][(*(False for _ in range(len(nodes))), 'AA')] = 0
state_max = dict()

for step in range(27):
    for state, cur_val in states[step].items():
        for end in nodes:
            if not state[nodes_ids[end]]:

                step_len = steps[state[-1], end]
                new_step = step + step_len + 1
                if new_step > 26:
                    continue

                new_state = list(state)
                new_state[-1] = end
                new_state[nodes_ids[end]] = True
                new_state = tuple(new_state)
                bool_state = tuple(new_state[:-1])

                new_val = cur_val + (26 - new_step) * nodes[end]
                if new_val > states[new_step].get(new_state, 0):
                    states[new_step][new_state] = new_val
                    if new_val > state_max.get(bool_state, 0):
                        state_max[bool_state] = new_val

print(
    max(
        state_max[s1] + state_max[s2]
        for s1, s2 in combinations(state_max, r=2)
        if not any(v1 and v2 for v1, v2 in zip(s1, s2))
    )
)