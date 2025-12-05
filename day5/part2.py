lines = [list(map(int, l.strip().split("-"))) for l in open(0) if l.strip()]

ranges = [l for l in lines if len(l) == 2]
values = [l[0] for l in lines if len(l) == 1]

last_end = 0
total = 0

for a, b in sorted(ranges):
    if b <= last_end:
        continue
    a = max(a, last_end + 1)
    total += b - a + 1
    last_end = b

print(total)
