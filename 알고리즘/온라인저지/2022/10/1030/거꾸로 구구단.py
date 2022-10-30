import sys

input = sys.stdin.readline

N, K = map(int, input().rstrip().split())
result = 0
for k in range(1, K+1):
    tmp = int(str(N*k)[::-1])
    result = max(result, tmp)
print(result)