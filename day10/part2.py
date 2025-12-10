import numpy as np
from scipy.optimize import milp, LinearConstraint

lines = [l.strip() for l in open(0) if l.strip()]

needed = 0
for l in lines:
    parts = [p[1:-1] for p in l.split()]

    size = len(parts[0])
    target = np.array(eval("[" + parts[-1] + "]"))
    vectors = [sum(1<<n for n in eval(f"[{p}]")) for p in parts[1:-1]]

    vectors = [np.array([int((n & (1 << i)) > 0) for i in range(size)]) for n in vectors]

    A = np.array(vectors).T
    b_l = target
    b_u = target
    integrality = np.ones(len(vectors))
    constraints = LinearConstraint(A, b_l, b_u)
    c = integrality

    needed += milp(c=c, constraints=constraints, integrality=integrality).fun

print(needed)
