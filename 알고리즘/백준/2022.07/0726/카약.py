R, C = map(int, input().split())
result = [0] * 9
arr = [input() for _ in range(R)]
rank = 1
for c in range(C-2, 0, -1):
    goal = False
    for r in range(R):
        if arr[r][c] != '.':
            tmp = int(arr[r][c])-1
            if not result[tmp]:
                result[tmp] += rank
                goal = True
    if goal:
        rank += 1
for r in result: print(r)