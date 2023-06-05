import sys

input = sys.stdin.readline

Q = int(input())
double = [2**i for i in range(32)]
for q in range(Q):
    A = int(input())
    print(1 if A in double else 0)