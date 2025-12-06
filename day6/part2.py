lines = [l[:-1] for l in open(0)]
maxlen = max(map(len, lines))
lines = [l + " " * (maxlen - len(l)) for l in lines]

numbers = []
total = 0
for l in reversed(list(zip(*lines))):
    l = "".join(l)
    if any(c in "0123456789" for c in l[:-1]):
        numbers += [int(l[:-1])]
    if l[-1] == "+":
        total += sum(numbers)
        numbers = []
    elif l[-1] == "*":
        tmp = 1
        for n in numbers:
            tmp *= n
        total += tmp
        numbers = []

print(total)
