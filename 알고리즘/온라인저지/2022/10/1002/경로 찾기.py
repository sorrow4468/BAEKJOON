import sys

input = sys.stdin.readline
INF = int(1e9)

N = int(input().rstrip())
arr = [list(map(int, input().rstrip().split())) for _ in [0]*N]
for k in range(N):
    for a in range(N):
        for b in range(N):
            if arr[a][k] and arr[k][b]: arr[a][b] = 1
for a in arr: print(*a)

# https://www.acmicpc.net/problem/11403