import sys

input = sys.stdin.readline

N, K = map(int, input().rstrip().split())
arr = []
for n in range(N): arr.append(list(map(int, input().rstrip().split())))
arr.sort(key=lambda x:(-x[1], -x[2], -x[3]))
prev = arr[0][1:]
rank = 1
step = 0
result = 1
for i in range(1, N):
    now = arr[i][1:]
    if now != prev: 
        rank += 1+step
        prev = now[:]
        step = 0
    else: step += 1
    if arr[i][0] == K: result = rank; break
print(result)