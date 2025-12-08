from math import hypot
from collections import Counter

lines = [list(map(int, l.strip().split(","))) for l in open(0) if l.strip()]

by_distance = []
for i, a in enumerate(lines):
    for j, b in enumerate(lines[:i]):
        by_distance.append((hypot(*[an - bn for an, bn in zip(a, b)]), i, j))

by_distance = iter(sorted(by_distance))

group_of = list(range(len(lines)))

for i in range(10 if len(lines) < 25 else 1000):
    dist, a, b = next(by_distance)

    g1, g2 = group_of[a], group_of[b]
    if g1 == g2:
        continue
    group_of = [g1 if g == g2 else g for g in group_of]

count = sorted(Counter(group_of).items(), key=lambda p: [p[1]])

(_, a), (_, b), (_, c) = count[-3:]
print(a*b*c)
