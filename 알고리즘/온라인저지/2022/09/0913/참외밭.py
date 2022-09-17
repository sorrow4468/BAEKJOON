K = int(input())
big = small = 1
lines = []
small_idx = []
for _ in range(6):
    lines.append(list(map(int, input().split())))
result = [[] for _ in range(4)]
while lines[2][0] != lines[4][0]:
    lines.append(lines.pop(0))
    lines.append(lines.pop(0))
for i in range(6):
    ewsn, length = lines[i][0], lines[i][1]
    ewsn -= 1
    if result[ewsn]:
        small_idx.append(ewsn)
    result[ewsn].append(length)
for r in result: 
    if len(r) == 1:
        big *= r[0]
i = 0
for s in small_idx[::-1]:
    small *= result[s][i]
    i += 1
print((big-small)*K)

# https://www.acmicpc.net/problem/2477