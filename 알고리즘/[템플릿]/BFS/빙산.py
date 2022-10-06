import sys
from collections import deque

input = sys.stdin.readline
dy, dx = [-1, 1, 0, 0], [0, 0, -1, 1]

def count_iceberg():
    Q = deque()
    visited = [[0]*M for _ in range(N)]
    iceberg = 0
    for i in range(N):
        for j in range(M):
            if arr[i][j] and not visited[i][j]:
                iceberg += 1
                Q.append((i, j))
                visited[i][j] = 1
                while Q:
                    y, x = Q.popleft()
                    for k in range(4):
                        ny, nx = y+dy[k], x+dx[k]
                        if 0<=ny<N and 0<=nx<M and not visited[ny][nx] and arr[ny][nx]:
                            Q.append((ny, nx))
                            visited[ny][nx] = 1
    return iceberg

def check_seawater():
    tmp_Q = deque()
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 0:
                tmp_Q.append((i, j))
    return tmp_Q

def melt_iceberg(seawater_Q):
    while seawater_Q:
        y, x = seawater_Q.popleft()
        for k in range(4):
            ny, nx = y+dy[k], x+dx[k]
            if 0<=ny<N and 0<=nx<M and arr[ny][nx]>0:
                arr[ny][nx] -= 1
    return

N, M = map(int, input().rstrip().split())
arr = [list(map(int, input().rstrip().split())) for _ in range(N)]
Q = deque()
result = 0
while count_iceberg() == 1:
    result += 1
    seawater_Q = check_seawater()
    melt_iceberg(seawater_Q)
if count_iceberg() == 0: print(0)
else: print(result)

"""
두 덩어리로 분리되는 최초의 시간을 구해야 한다
끝까지 두덩이가 되지 않고 통째로 녹아버린다면 0을 출력
"""

# https://www.acmicpc.net/problem/2573