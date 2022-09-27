import sys

input = sys.stdin.readline

N = int(input().rstrip())
for i in sorted([int(input().rstrip()) for _ in [0]*(N)]): print(i)