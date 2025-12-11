from collections import defaultdict
from functools import cache

lines = [l.strip() for l in open(0) if l.strip()]

succ = defaultdict(list)

for l in lines:
    dst, srcs = l.split(": ")
    succ[dst] = srcs.split()

@cache
def num_paths(src, has_dac, has_fft):
    if src == "out": return has_dac * has_fft
    return sum(num_paths(s, has_dac or src == "dac", has_fft or src == "fft") for s in succ[src])

print(num_paths("svr", False, False))
