from itertools import combinations
import sys
with open(sys.argv[1] if len(sys.argv) > 1 else sys.argv[0][-5:-3] + ".in") as file:
    data = file.readlines()
    data = [line.strip() for line in data]
    data = [line.split(",") for line in data]
    data = [tuple(int(x) for x in line) for line in data]

p1 = 0
p2 = 0


def distance_squared(a, b):
    assert len(a) == len(b), "Points must have the same dimension"
    return (sum((x - y)**2 for x, y in zip(a, b)))


dists = []
for a, b in combinations(data, 2):
    dists.append((distance_squared(a, b), a, b))

dists.sort()

circuit_index = 0
point_to_circuit = {}
for dist, a, b in dists[:1000]:
    if a in point_to_circuit and b in point_to_circuit:
        if point_to_circuit[a] != point_to_circuit[b]:
            old_circuit = point_to_circuit[b]
            for key in point_to_circuit:
                if point_to_circuit[key] == old_circuit:
                    point_to_circuit[key] = point_to_circuit[a]

    elif a not in point_to_circuit and b not in point_to_circuit:
        point_to_circuit[a] = circuit_index
        point_to_circuit[b] = circuit_index
        circuit_index += 1

    elif a in point_to_circuit:
        point_to_circuit[b] = point_to_circuit[a]

    else:
        point_to_circuit[a] = point_to_circuit[b]

circuits = [[] for _ in range(circuit_index)]
for key, value in point_to_circuit.items():
    circuits[value].append(key)
while [] in circuits:
    circuits.remove([])
p1 = 1
for l in sorted(map(len, circuits), reverse=True)[:3]:
    p1 *= l
print("Part 1:", p1)


circuit_index = 0
point_to_circuit = {}
circuits = {}
for dist, a, b in dists:
    if a in point_to_circuit and b in point_to_circuit:
        if point_to_circuit[a] != point_to_circuit[b]:
            old_circuit = point_to_circuit[b]
            for key in point_to_circuit:
                if point_to_circuit[key] == old_circuit:
                    point_to_circuit[key] = point_to_circuit[a]
                    circuits[point_to_circuit[a]].append(key)
            del circuits[old_circuit]

    elif a not in point_to_circuit and b not in point_to_circuit:
        point_to_circuit[a] = circuit_index
        point_to_circuit[b] = circuit_index
        circuits[circuit_index] = [a, b]
        circuit_index += 1

    elif a in point_to_circuit:
        point_to_circuit[b] = point_to_circuit[a]
        circuits[point_to_circuit[a]].append(b)

    else:
        point_to_circuit[a] = point_to_circuit[b]
        circuits[point_to_circuit[b]].append(a)

    if any(len(c) == 1000 for c in circuits.values()):
        p2 = a[0]*b[0]
        break


print("Part 2:", p2)
