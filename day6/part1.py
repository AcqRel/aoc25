lines = [l.strip().split() for l in open(0)]

total = 0
for l in list(zip(*lines)):
    if l[-1] == "+":
        total += sum(map(int, l[:-1]))
    else:
        tmp = 1
        for n in l[:-1]:
            tmp *= int(n)
        total += tmp


print(total)
