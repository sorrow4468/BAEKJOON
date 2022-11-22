import sys

input = sys.stdin.readline

for _ in range(int(input().rstrip())):
    N, C = map(int, input().rstrip().split())
    print((N-1)//C + 1)