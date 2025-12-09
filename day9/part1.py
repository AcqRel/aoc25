lines = [list(map(int,l.strip().split(","))) for l in open(0) if l.strip()]

maximum = 0

for x1, y1 in lines:
    for x2, y2 in lines:
        maximum = max(maximum, (abs(x1 - x2) + 1) * (abs(y1 - y2) + 1))

print(maximum)
