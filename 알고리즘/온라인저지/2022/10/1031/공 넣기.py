import sys

input = sys.stdin.readline

N, M = map(int, input().rstrip().split())
result = [0]*N
for m in range(M):
    a, b, c = map(int, input().rstrip().split())
    for i in range(a-1, b):
        result[i] = c
print(*result)