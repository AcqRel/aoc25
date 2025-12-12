"""

Infeasible attempt because the SAT solver doesn't seem to handle the problem well.

"""

from itertools import product
import subprocess

lines = open(0).read().strip()

groups = [g.split("\n") for g in lines.split("\n\n")]

shapes, cases = groups[:-1], groups[-1]

shapes = ["".join(s[1:]) for s in shapes]

orientations = [
    [0, 1, 2, 3, 4, 5, 6, 7, 8],
    [2, 1, 0, 5, 4, 3, 8, 7, 6],
    [6, 7, 8, 3, 4, 5, 0, 1, 2],
    [8, 7, 6, 5, 4, 3, 2, 1, 0],
    [0, 3, 6, 1, 4, 7, 2, 5, 8],
    [6, 3, 0, 7, 4, 1, 8, 5, 2],
    [1, 4, 7, 2, 5, 8, 0, 3, 6],
    [7, 4, 1, 8, 5, 2, 6, 3, 0],
]

for case in cases:
    i = 0
    def next_var():
        global i
        i += 1
        return "x" + str(i)

    size, num = case.split(": ")
    width, height = map(int, size.split("x"))
    num = list(map(int, num.split()))

    cells_at = [[[] for _ in range(width)] for _ in range(height)]
    constraints = []

    for shape, minimum in zip(shapes, num):

        placed = []
        for mapping, y, x in product(orientations, range(height - 2), range(width - 2)):
            coords = [(x+x2, y+y2) for y2 in range(3) for x2 in range(3) if shape[mapping[y2*3+x2]] == "#"]
            var = next_var()

            for (x, y) in coords:
                cells_at[y][x].append(var)

            placed.append(var)

        constraints.append(" ".join(f"1 {var}" for var in placed) + f" >= {minimum}")


    for row in cells_at:
        for cell in row:
            constraints.append(" ".join(f"-1 {var}" for var in cell) + " >= -1")

    with open("/tmp/solve.opb", "w") as f:
        f.write(f"* #variable= {i} #constraint= {len(constraints)}\n")
        for c in constraints:
            f.write(c + "\n")

    subprocess.run(["roundingsat", "/tmp/solve.opb"])
