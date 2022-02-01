import sys

def input():
    return sys.stdin.readline()

dp = [0] * 10001

N = int(input())

for n in range(N):
    dp[int(input())] += 1

for i in range(1, 10001):
    if dp[i]:
        for j in range(dp[i]):
            print(i)