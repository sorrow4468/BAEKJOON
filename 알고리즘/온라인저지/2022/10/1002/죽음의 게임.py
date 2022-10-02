import sys

input = sys.stdin.readline

N, K = map(int, input().rstrip().split())
death = [int(input().rstrip()) for _ in range(N)]
result = 0
i = 0
visited = [0]*N
while i != K:
    if not visited[i]:
        visited[i] = 1
        i = death[i]
        result += 1
    else: 
        print(-1)
        exit()
print(result)