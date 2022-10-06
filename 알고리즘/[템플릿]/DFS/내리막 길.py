import sys

input = sys.stdin.readline
dy, dx = [-1, 1, 0, 0], [0, 0, -1, 1]

def dfs(y, x):
    if y == N-1 and x == M-1: return 1
    if visited[y][x] != -1: return visited[y][x]
    visited[y][x] = 0
    for i in range(4):
        ny, nx = y+dy[i], x+dx[i]
        if 0<=ny<N and 0<=nx<M:
            if arr[ny][nx] < arr[y][x]:
                visited[y][x] += dfs(ny, nx)
    return visited[y][x]

N, M = map(int, input().rstrip().split())
arr = [list(map(int, input().rstrip().split())) for _ in range(N)]
visited = [[-1]*M for _ in range(N)]
print(dfs(0, 0))

"""
탐색하면서 처리하는 방문 배열이 그냥 배열이 아닌 DP배열이다
1.방문배열 초기화는 -1
2.방문처리는 0
3.해당 지점을 경유하여 목적지에 도달 가능한 경로 경우의 수
등으로 방문배열을 채워나간다
3번이 채워지는 원리가 신박하다
목적지에 도달할 경우 line 7을 통해서
지나온 모든 경로에 1을 더해준다
결과적으로 시작점에서 봤을 때
목적지까지 갈 수 있는 경로의 수가 visited[0][0]에 들어오게 된다

<참고한 링크>
https://ca.ramel.be/70
"""

# https://www.acmicpc.net/problem/1520