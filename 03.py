import sys
with open(sys.argv[1] if len(sys.argv) > 1 else sys.argv[0][-5:-3] + ".in") as file:
    data = file.readlines()
    data = [line.strip() for line in data]
    banks = [[int(x) for x in line] for line in data]


def find_joltage(n):
    res = 0
    for bank in banks:
        maxs = [0 for _ in range(n)]
        indices = [0 for _ in range(n)]

        for i in range(n):
            start = indices[i-1] + 1 if i > 0 else 0
            end = len(bank) - ((n-1) - i)  # Leave enough room for the next digits
            for j in range(start, end):
                if bank[j] > maxs[i]:
                    maxs[i] = bank[j]
                    indices[i] = j

        res += int("".join(map(str, maxs)))
    return res


print("Part 1:", find_joltage(2))
print("Part 2:", find_joltage(12))
