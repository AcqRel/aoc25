from collections import defaultdict

lines = [l.strip() for l in open(0)]

beams = {i:1 for i, c in enumerate(lines[0]) if c == "S"}

for l in lines[1:]:
    splitters = set(i for i, c in enumerate(l) if c == "^")

    new_beams = defaultdict(int)
    for beam, count in beams.items():
        if l[beam] == ".":
            new_beams[beam] += count
        if l[beam] == "^":
            new_beams[beam - 1] += count
            new_beams[beam + 1] += count
    beams = new_beams

print(sum(beams.values()))
