import re
from itertools import chain

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

states = [dict() for _ in range(31)]
states[0][(*(False for _ in range(len(nodes))), 'AA')] = 0

for step in range(31):
    for state, cur_val in states[step].items():
        for end in nodes:
            if not state[nodes_ids[end]]:

                step_len = steps[state[-1], end]
                new_step = step + step_len + 1
                if new_step > 30:
                    continue

                new_state = list(state)
                new_state[-1] = end
                new_state[nodes_ids[end]] = True
                new_state = tuple(new_state)

                new_val = cur_val + (30 - new_step) * nodes[end]
                if new_val > states[new_step].get(new_state, 0):
                    states[new_step][new_state] = new_val

print(max(chain.from_iterable(step.values() for step in states)))
