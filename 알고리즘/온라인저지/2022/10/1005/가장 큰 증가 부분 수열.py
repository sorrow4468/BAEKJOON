import sys

input = sys.stdin.readline

N = int(input().rstrip())
arr = list(map(int, input().rstrip().split()))
dp = arr[:]
for i in range(N):
    for j in range(i):
        if arr[j] < arr[i]:
            dp[i] = max(dp[i], dp[j]+arr[i])
print(max(dp))