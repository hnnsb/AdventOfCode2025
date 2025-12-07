from copy import deepcopy
from functools import cache, lru_cache
import sys
with open(sys.argv[1] if len(sys.argv) > 1 else sys.argv[0][-5:-3] + ".in") as file:
    data = file.readlines()
    data = [line.strip() for line in data]

data = [list(line) for line in data]
sr, sc = (0, data[0].index('S'))
data[sr][sc] = '|'
diagram = deepcopy(data)

p1 = 0
p2 = 0

R, C = (len(data), len(data[0]))
r = 1
while r < R:
    for c in range(C):
        if data[r-1][c] == '|':
            if data[r][c] == '.':
                data[r][c] = '|'
            elif data[r][c] == '^':
                p1 += 1
                data[r][c-1] = '|'
                data[r][c+1] = '|'
    r += 1

print("Part 1:", p1)


@cache
def step(r, c):
    if r == R-1:
        return 1
    if diagram[r+1][c] == '.':
        return step(r+1, c)
    elif diagram[r+1][c] == '^':
        return step(r+1, c-1) + step(r+1, c+1)
    return 0


p2 = step(sr, sc)

print("Part 2:", p2)
