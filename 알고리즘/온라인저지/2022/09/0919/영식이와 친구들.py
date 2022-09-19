import sys

input = sys.stdin.readline

N, M, L = map(int, input().rstrip().split())
arr = [0]*N
arr[0] += 1
result = 0
now = 0
while max(arr)<M:
    if arr[now]%2:
        now += L
        now %= N
        arr[now] += 1
    else:
        now -= L
        now += N
        now %= N
        arr[now] += 1
    result += 1
print(result)