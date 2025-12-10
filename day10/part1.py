from itertools import combinations

lines = [l.strip() for l in open(0) if l.strip()]

needed = 0
for l in lines:
    parts = [p[1:-1] for p in l.split()]

    target = sum((c == "#") << i for i, c in enumerate(parts[0]))
    parts = [sum(1<<n for n in eval(f"[{p}]")) for p in parts[1:]]

    for n in range(len(parts)):
        for comb in combinations(parts[:-1], n):

            xored = 0
            for m in comb:
                xored ^= m

            if xored == target:
                break
        else:
            continue
        needed += n
        break

print(needed)
