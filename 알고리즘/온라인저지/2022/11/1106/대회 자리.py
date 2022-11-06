import sys

input = sys.stdin.readline

for _ in range(int(input().rstrip())):
    P, M = map(int, input().rstrip().split())
    result = set()
    for p in range(P):
        result.add(int(input().rstrip()))
    print(P-len(result))