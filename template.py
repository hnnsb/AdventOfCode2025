import sys
with open(sys.argv[1] if len(sys.argv) > 1 else sys.argv[0][-5:-3] + ".in") as file:
    data = file.readlines()

p1 = 0
p2 = 0
print("Part 1:", p1)
print("Part 2:", p2)
