import sys

input = sys.stdin.readline

N = int(input().rstrip())
for i in sorted([int(input()) for _ in [0]*N], reverse=True): print(i)
