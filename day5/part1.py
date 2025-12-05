lines = [list(map(int, l.strip().split("-"))) for l in open(0) if l.strip()]

ranges = [l for l in lines if len(l) == 2]
values = [l[0] for l in lines if len(l) == 1]

print(sum(any(a <= n <= b for a, b in ranges) for n in values))
