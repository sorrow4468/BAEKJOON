import sys

input = sys.stdin.readline

S = input().rstrip()
for s in S:
    print(s.upper(), end='')