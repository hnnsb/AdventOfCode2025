from collections import deque
import pulp as pl
import sys
with open(sys.argv[1] if len(sys.argv) > 1 else sys.argv[0][-5:-3] + ".in") as file:
    data = file.readlines()
    data = [line.strip() for line in data]

p1 = 0
p2 = 0


def part1():
    res = 0
    for index, line in enumerate(data):
        print(f"{index/len(data)*100:.2f}%", end="\r")
        l = line.split(" ")
        target = l[0]
        buttons = l[1:-1]
        joltage = l[-1]
        target = [x == "#" for x in target.strip("[]")]
        buttons = [tuple(map(int, x.strip("()").split(","))) for x in buttons]

        current = [False for _ in range(len(target))]
        best = 1e9
        q = deque()
        q.append((current, 0, None))
        while q:
            state, steps, last_button = q.popleft()
            if steps >= best:
                continue
            if state == target:
                best = min(best, steps)
                continue
            for b in buttons:
                if b == last_button:
                    continue
                new = state[:]
                for i in b:
                    new[i] = not new[i]
                q.append((new, steps + 1, b))

        assert best != 1e9
        res += best

    print(f"{100:.2f}%")
    return res


print("Part 1:", part1())

for index, line in enumerate(data):
    print(f"{index/len(data)*100:.2f}%", end="\r")
    l = line.split(" ")
    buttons = l[1:-1]
    joltage = l[-1]
    buttons = [tuple(map(int, x.strip("()").split(","))) for x in buttons]
    joltage = [int(x) for x in joltage.strip("{}").split(",")]

    prob = pl.LpProblem("MinSteps", pl.LpMinimize)

    button_vars = pl.LpVariable.dicts("Button", range(len(buttons)), lowBound=0, cat=pl.LpInteger)
    prob += pl.lpSum([button_vars[i] for i in range(len(buttons))]), "Minimize number of button presses"

    for i, j in enumerate(joltage):
        prob += (
            pl.lpSum([button_vars[b] for b in range(len(buttons)) if i in buttons[b]]) == j,
            f"Joltage_constraint_{i}",
        )

    prob.solve(pl.PULP_CBC_CMD(msg=False))
    p2 = pl.value(prob.objective)

print(f"{100:.2f}%")

print("Part 2:", int(p2))
