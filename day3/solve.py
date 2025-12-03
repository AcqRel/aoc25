from functools import cache

t1 = 0
t2 = 0
for l in open(0):
    l = l.strip()

    @cache
    def max_for(i, n):
        if n == 0:
            return ""
        if i + n == len(l):
            return l[i:]
        with_here = l[i] + max_for(i+1, n-1)
        without_here = max_for(i+1, n)
        return max(with_here, without_here)

    t1 += int(max_for(0, 2))
    t2 += int(max_for(0, 12))

print(t1, t2)
