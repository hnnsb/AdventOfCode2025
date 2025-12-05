from copy import deepcopy
import sys

from helper.grid import NDMatrix

with open(sys.argv[1] if len(sys.argv) > 1 else sys.argv[0][-5:-3] + ".in") as file:
    data = file.readlines()
    data = [line.strip() for line in data]
    data = [[c for c in line] for line in data]

res = 0
grid = NDMatrix(data)
R, C = grid.dim
changed = True
grid_altered = deepcopy(grid)

first_iteration = True
while changed:
    changed = False
    for r in range(R):
        for c in range(C):
            if grid[r, c] == ".":
                continue
            count = 0
            for nr, nc in grid.all_neighbours(r, c):
                if grid[nr, nc] == '@':
                    count += 1
            if count < 4:
                changed = True
                grid_altered[r, c] = '.'
                res += 1

    if first_iteration:
        print("Part 1:", res)
        first_iteration = False

    grid = deepcopy(grid_altered)

print("Part 2:", res)
