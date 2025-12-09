lines = [list(map(int,l.strip().split(","))) for l in open(0) if l.strip()]

maximum = 0

w = max(x for x, y in lines) + 1
h = max(y for x, y in lines) + 1

l = [set() for _ in range(h)]
r = [set() for _ in range(h)]

for (x1, y1), (x2, y2) in zip(lines, lines[1:]+lines[:1]):
    if x1 == x2:
        if y2 > y1:
            for y in range(y1, y2 + 1):
                r[y].add(x1)
        elif y2 < y1:
            for y in range(y2, y1 + 1):
                l[y].add(x1)
    else:
        from_l = x2 > x1

if min(l[-1]) > min(r[-1]):
    l, r = r, l

ranges = []
for lrow, rrow in zip(l, r):
    lrow = [(x, "l") for x in lrow]
    rrow = [(x, "r") for x in rrow]
    row = sorted(lrow + rrow)

    in_range = False
    rranges = []
    for x, c in row:
        if c == "l":
            if not in_range:
                if not rranges or rranges[-1][1] != x - 1:
                    rranges += [[x, x]]
                in_range = True
        if c == "r":
            rranges[-1][1] = x
            in_range = False
    ranges += [rranges]

maximum = 0
for i, (x1, y1) in enumerate(lines):
    print(i, len(lines))
    for x2, y2 in lines:
        if not any(l <= min(x1, x2) and max(x1, x2) <= r for l, r in ranges[y1]):
            continue
        if not any(l <= min(x1, x2) and max(x1, x2) <= r for l, r in ranges[y2]):
            continue
        for y in range(min(y1, y2), max(y1, y2) + 1):
            if not any(l <= min(x1, x2) and max(x1, x2) <= r for l, r in ranges[y]):
                break
        else:
            maximum = max(maximum, (abs(x1 - x2) + 1) * (abs(y1 - y2) + 1))

print(maximum)
