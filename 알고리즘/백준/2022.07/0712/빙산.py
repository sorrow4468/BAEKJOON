"""
기준 : 바다or빙산
바다를 발견하면 주위 빙산을 녹이기
    녹이다보면 바다는 늘어나서 탐색범위가 증가한다
    하지만 두 덩이만 나누면 되니 크게 증가하지 않을 수 있다
빙산을 발견하면 주위 바다만큼 녹이기
    처음엔 빙산이 더 많을 것이고, 탐색범위 시작이 크다
    다만 녹여갈수록 탐색범위가 줄어들 것이다
매번 녹일 때 마다 두 덩이가 되었는지 확인하고 해당 횟수를 출력
0을 출력하는 경우는, 다 녹일 때 까지 분리되지 않고 한 덩이인 경우
처음엔 바다를 기준으로 진행하는게 빠를거고
회를 거듭할수록 빙산을 기준으로 진행하는게 빠를거다
바다를 기준으로 진행하는걸 먼저 구현하고
시간이 모자라면 빙산기준도 구현해서 1000회쯤부터 빙산기준으로 진행하자
라고 할려 했는데, 해보니까 빙산이 녹은자리가 바다가 되어 연쇄적으로 녹이는데
그건 잘못됐고
빙산기준으로 하는게 맞겠다
아니다 빙산기준으로 해도 연쇄적으로 녹는건 피할 수 없었다
뭔가 다른 방법을 통해서 연쇄적으로 녹는 것을 피해야 하는데...
"""
from collections import deque


def iceberg_count():
    visited = [[0]*M for _ in range(N)]
    tmp = 0
    for i in range(N):
        for j in range(M):
            if arr[i][j] and not visited[i][j]:
                tmp += 1
                Q = deque()
                Q.append((i, j))
                while Q:
                    y, x = Q.popleft()
                    visited[y][x] = 1
                    for i in range(4):
                        ny = y+dy[i]
                        nx = x+dx[i]
                        if 0<=ny<N and 0<=nx<M and not visited[ny][nx]:
                            Q.append((ny, nx))
    return tmp


def melt(): # 얼음 기준
    tmp_arr = [[0]*M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if arr[i][j]:
                tmp = 0
                for k in range(4):
                    ny = i+dy[k]
                    nx = i+dx[k]
                    if 0<=ny<N and 0<=nx<M and arr[ny][nx] == 0:
                        tmp += 1
                tmp_arr[i][j] = tmp
    for t in tmp_arr: print(t)
    for i in range(N):
        for j in range(M):
            arr[i][j] -= tmp_arr[i][j]
            if arr[i][j] < 0:
                arr[i][j] = 0


dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
# for a in arr: print(a)
result = 0
# print(iceberg_count())
while iceberg_count() == 1:
    result += 1
    melt()
    for a in arr: print(a)
    print()
print(result)