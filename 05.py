import sys

with open(sys.argv[1] if len(sys.argv) > 1 else sys.argv[0][-5:-3] + ".in") as file:
    data = file.read()
    ranges, ids = data.split("\n\n")
    ranges = ranges.split("\n")
    ranges = [tuple(map(int, r.split("-"))) for r in ranges]
    ids = ids.split("\n")
    ids = [int(i) for i in ids]

p1 = 0
p2 = 0

for id in ids:
    if any(start <= id <= end for start, end in ranges):
        p1 += 1

print("Part 1:", p1)

ranges = sorted(ranges)
i = 0
while i < len(ranges)-1:
    a, b = ranges[i]
    x, y = ranges[i+1]

    if b > y:
        new = a, b
        ranges = ranges[:i]+[new]+ranges[i+2:]

    elif x <= b <= y:
        new = a, y
        ranges = ranges[:i]+[new]+ranges[i+2:]

    else:
        i += 1

p2 = sum([b-a+1 for a, b in ranges])
print("Part 2:", p2)
