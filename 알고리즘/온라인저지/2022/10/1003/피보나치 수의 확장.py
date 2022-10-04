import sys

input = sys.stdin.readline
mod = int(1e9)

N = int(input().rstrip())
a, b = 1, 1
for _ in range(abs(N)-2): a, b = b, (a+b)%mod
if abs(N)%2 == 0 and N < 0: print(-1)
elif N == 0: print(0)
else: print(1)
print(b if N != 0 else 0)

"""
문제를 잘 보자
1,000,000,007로 나누는 문제가 많았다고 해서
모든 문제들이 그런 것은 아니다
1,000,000,000으로 나누면 되는걸로 
문제 제대로 안읽고 몇분을 날린거냐..
"""

# https://www.acmicpc.net/problem/1788