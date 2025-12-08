from math import hypot

lines = [list(map(int, l.strip().split(","))) for l in open(0) if l.strip()]

by_distance = []
for i, a in enumerate(lines):
    for j, b in enumerate(lines[:i]):
        by_distance.append((hypot(*[an - bn for an, bn in zip(a, b)]), i, j))

by_distance = sorted(by_distance)

group_of = list(range(len(lines)))

last_prod = 0

for dist, a, b in by_distance:
    g1, g2 = group_of[a], group_of[b]
    if g1 == g2:
        continue
    group_of = [g1 if g == g2 else g for g in group_of]
    last_prod = lines[a][0] * lines[b][0]

print(last_prod)
