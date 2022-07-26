import sys

input = sys.stdin.readline

N = int(input())
P = sorted(list(map(int, input().split())))
result, S = 0, sum(P)
for p in P:
    result += p * (S-p)
    S -= p
print(result)