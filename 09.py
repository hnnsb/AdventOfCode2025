from itertools import combinations
import sys
with open(sys.argv[1] if len(sys.argv) > 1 else sys.argv[0][-5:-3] + ".in") as file:
    data = file.readlines()
    data = [line.strip() for line in data]
    data = [line.split(",") for line in data]
    data = [tuple(int(x) for x in line) for line in data]

p1 = 0
p2 = 0


def area(input):
    (a, b), (x, y) = input
    w = abs(a-x)+1
    h = abs(b-y)+1
    return w*h


p1 = max(map(area, combinations(data, 2)))
print("Part 1:", p1)
