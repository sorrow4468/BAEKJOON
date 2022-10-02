import sys

input = sys.stdin.readline

for _ in [0]*int(input().rstrip()):
    result = 0
    N = int(input().rstrip())
    death = [int(input().rstrip())-1 for _ in range(N)]
    visited = [0]*N
    i = 0
    flag = True
    while i != N-1:
        if not visited[i]:
            visited[i] = 1
            i = death[i]
            result += 1
        else: flag = False; break
    if flag: print(result)
    else: print(0)