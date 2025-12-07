lines = [l.strip() for l in open(0)]

beams = set(i for i, c in enumerate(lines[0]) if c == "S")

total = 0

for l in lines[1:]:
    splitters = set(i for i, c in enumerate(l) if c == "^")
    splits = beams & splitters
    total += len(splits)
    kept = beams - splitters
    beams = kept | set(n - 1 for n in splits) | set(n + 1 for n in splits)

print(total)