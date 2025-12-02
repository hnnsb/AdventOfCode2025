import sys

with open(sys.argv[1] if len(sys.argv) > 1 else sys.argv[0][-5:-3] + ".in") as file:
    data = file.read()
data = data.split(",")
data = [tuple(map(int, x.split("-"))) for x in data]

p1 = 0
p2 = 0
for a, b in data:
    for id in range(a, b + 1):
        num = str(id)
        length = len(num)
        if num[:length//2] == num[length//2:]:
            p1 += id

        for pattern_length in range(1, length):
            if length % pattern_length != 0:
                continue

            parts = [num[j:j+pattern_length] for j in range(0, len(num), pattern_length)]

            if all([parts[0] == part for part in parts[1:]]):
                p2 += id
                break


print("Part 1:", p1)
print("Part 2:", p2)
