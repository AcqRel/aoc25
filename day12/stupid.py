possible = 0
for line in open(0):
    if "x" in line:
        size, num = line.split(": ")
        width, height = map(int, size.split("x"))
        possible += width * height >= 9 * sum(map(int, num.split()))
print(possible)
