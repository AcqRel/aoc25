
pos = 50
count = 0
for l in open(0):
    if l[0] == "L":
        for i in range(int(l[1:].strip())):
            pos -= 1
            count += (pos % 100 == 0)
    else:
        for i in range(int(l[1:].strip())):
            pos += 1
            count += (pos % 100 == 0)

print(count)
