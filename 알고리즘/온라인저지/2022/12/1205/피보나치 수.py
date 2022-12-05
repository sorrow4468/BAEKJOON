import sys

input = sys.stdin.readline

N = int(input().rstrip())
mod = int(1e9)+7
a, b = 1, 1
for _ in range(N-2): a, b = b, (a+b)
print(b)