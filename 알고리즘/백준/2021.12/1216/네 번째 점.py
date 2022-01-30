xdots = [0 for _ in range(1001)]
ydots = [0 for _ in range(1001)]

for _ in range(3):
    x, y = map(int, input().split())
    xdots[x] += 1
    ydots[y] += 1

result = []

for xdot in xdots:
    if xdot == 1:
        result.append(xdots.index(xdot))

for ydot in ydots:
    if ydot == 1:
        result.append(ydots.index(ydot))

for r in result:
    print(r, end=' ')