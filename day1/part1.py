
pos = 50
count = 0
for l in open(0):
    if l[0] == "L":
        pos -= int(l[1:].strip())
    else:
        pos += int(l[1:].strip())
    count += (pos % 100 == 0)

print(count)
