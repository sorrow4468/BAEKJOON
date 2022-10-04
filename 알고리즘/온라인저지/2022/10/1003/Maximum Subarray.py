import sys

input = sys.stdin.readline

for _ in [0]*int(input().rstrip()):
    N = int(input().rstrip())
    arr = list(map(int, input().rstrip().split()))
    dp = [0]*N
    dp[0] = arr[0]
    for i in range(1, N):
        dp[i] = max(dp[i-1]+arr[i], arr[i])
    print(max(dp))