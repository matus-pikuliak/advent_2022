import re


def get_best(ore_ore, clay_ore, obs_ore, obs_clay, geo_ore, geo_obs, num_generations):

    generation = {(0, 0, 0, 0, 1, 0, 0)}

    max_ore = max(ore_ore, clay_ore, obs_ore, geo_ore)

    for generation_idx in range(num_generations - 1):

        new_generation = set()

        for ore, clay, obs, geo, rore, rclay, robs in generation:
            new_generation.add((ore + rore, clay + rclay, obs + robs, geo, rore, rclay, robs))
            if ore - ore_ore >= 0 and rore + 1 <= max_ore:
                new_generation.add((ore + rore - ore_ore, clay + rclay, obs + robs, geo, rore + 1, rclay, robs))
            if ore - clay_ore >= 0 and rclay + 1 <= obs_clay:
                new_generation.add((ore + rore - clay_ore, clay + rclay, obs + robs, geo, rore, rclay + 1, robs))
            if ore - obs_ore >= 0 and clay - obs_clay >= 0 and robs + 1 <= geo_obs:
                new_generation.add((ore + rore - obs_ore, clay + rclay - obs_clay, obs + robs, geo, rore, rclay, robs + 1))
            if ore - geo_ore >= 0 and obs - geo_obs >= 0:
                new_geo = num_generations - generation_idx - 1
                new_generation.add((ore + rore - geo_ore, clay + rclay, obs + robs - geo_obs, geo + new_geo, rore, rclay, robs))

        max_geo = max(g[3] for g in new_generation)
        k = num_generations - generation_idx
        min_geo = max_geo - k * (k - 1) // 2
        generation = {g for g in new_generation if g[3] >= min_geo}

    return max_geo


part_1 = 0
for line_idx, line in enumerate(open('input')):
    nums = list(map(int, re.findall(r'\d+', line)))
    part_1 += int(nums[0]) * get_best(*nums[1:], 24)
print(part_1)

part_2 = 1
for line_idx, line in enumerate(open('input')):
    nums = list(map(int, re.findall(r'\d+', line)))
    part_2 *= get_best(*nums[1:], 32)
    if line_idx == 2:
        break
print(part_2)

