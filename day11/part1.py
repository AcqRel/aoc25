from collections import defaultdict
from functools import cache

lines = [l.strip() for l in open(0) if l.strip()]

succ = defaultdict(list)

for l in lines:
    dst, srcs = l.split(": ")
    succ[dst] = srcs.split()

@cache
def num_paths(src):
    if src == "out": return 1
    return sum(num_paths(s) for s in succ[src])

print(num_paths("you"))
