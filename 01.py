import sys

with open(sys.argv[1] if len(sys.argv) > 1 else sys.argv[0][-5:-3] + ".in") as file:
    data = file.readlines()
    steps = [line.strip() for line in data]

DIR = {"L": -1, "R": 1}
prev = 50
pos = 50
p1 = 0
p2 = 0
for step in steps:
    dir = step[0]
    amount = int(step[1:])
    for i in range(amount):
        pos += DIR[dir]
        pos %= 100
        if pos == 0:
            p2 += 1

    if pos == 0:
        p1 += 1

print("Part 1:", p1)
print("Part 2:", p2)
