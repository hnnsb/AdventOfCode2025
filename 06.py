import sys
with open(sys.argv[1] if len(sys.argv) > 1 else sys.argv[0][-5:-3] + ".in") as file:
    data = file.readlines()
    data = [line.strip() for line in data]

data = [line.split() for line in data]
ops = data[-1]
numbers = data[:-1]
numbers = [[int(x) for x in line] for line in numbers]

p1 = 0
p2 = 0

R = len(numbers)
C = len(numbers[0])
for c in range(C):
    col = [numbers[r][c] for r in range(R)]
    res = 0
    match ops[c]:
        case '+':
            res = sum(col)
        case '*':
            res = 1
            for x in col:
                res *= x
    p1 += res

print("Part 1:", p1)

with open(sys.argv[1] if len(sys.argv) > 1 else sys.argv[0][-5:-3] + ".in") as file:
    data = file.readlines()
    data = [line.strip("\n") for line in data]
    ops = data[-1]
    data = data[:-1]
ops = list(reversed(ops.split()))
data = [list(reversed(line)) for line in data]

C = len(data[0])
R = len(data)
numbers = []
i = 0
current_numbers = []

for c in range(C):
    digits = ""
    for r in range(R):
        digits += data[r][c]

    if all([n == " " for n in digits]):
        numbers.append(current_numbers)
        current_numbers = []
    else:
        current_numbers.append(int(digits))
numbers.append(current_numbers)

for i, col in enumerate(numbers):
    res = 0
    match ops[i]:
        case '+':
            res = sum(col)
        case '*':
            res = 1
            for x in col:
                res *= x
    p2 += res

print("Part 2:", p2)
