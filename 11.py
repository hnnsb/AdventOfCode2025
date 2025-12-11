from functools import cache
import sys
with open(sys.argv[1] if len(sys.argv) > 1 else sys.argv[0][-5:-3] + ".in") as file:
    data = file.readlines()
    data = [line.strip() for line in data]
data = [line.split(": ") for line in data]
data = {line[0]: line[1].split(" ") for line in data}
p1 = 0
p2 = 0

start = "you"
Q = [(start, 0)]
while Q:
    node, dist = Q.pop(0)
    if node == "out":
        p1 += 1
        continue

    for neighbor in data[node]:
        Q.append((neighbor, dist + 1))

print("Part 1:", p1)


@cache
def countTails(node, gotFFT, gotDAC):
    connections = data[node]
    if "out" in connections and gotFFT and gotDAC:
        return 1
    elif "out" in connections:
        return 0

    if node == "fft":
        gotFFT = True
    if node == "dac":
        gotDAC = True

    count = 0
    for neighbor in connections:
        count += countTails(neighbor, gotFFT, gotDAC)
    return count


p2 = countTails("svr", False, False)
print("Part 2:", p2)
