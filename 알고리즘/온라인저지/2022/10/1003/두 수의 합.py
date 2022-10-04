import sys

input = sys.stdin.readline

N = int(input().rstrip())
arr = sorted(list(map(int, input().rstrip().split())))
K = int(input().rstrip())
result = 0
start, end = 0, N-1
while start<end:
    tmp = arr[start]+arr[end]
    if tmp > K: end -= 1
    elif tmp < K: start += 1
    else: result += 1; start += 1
print(result)