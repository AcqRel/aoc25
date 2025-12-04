lines = [list(l.strip()) for l in open(0)]

out = 0

while True:
    any_new = 0
    for y, row in enumerate(lines):
        for x, cell in enumerate(row):
            count=0
            for y2 in [y-1, y, y+1]:
                for x2 in [x-1, x, x+1]:
                    if 0 <= y2 < len(lines) and 0 <= x2 < len(lines[y2]) and lines[y2][x2] == "@":
                        count += 1
            valid = (count < 5) and cell == "@"
            if valid:
                any_new = True
                lines[y][x] = "."
                out += valid

            print(("x" if valid else cell), end="")
        print()
    print()

    if not any_new:
        break

print(out)
