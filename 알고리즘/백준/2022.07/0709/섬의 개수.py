from collections import deque


def bfs(y, x):
    Q.append((y, x))
    while Q:
        y, x = Q.popleft()
        if arr[y][x] == 0:
            continue
        arr[y][x] = 0
        for i in range(8):
            ny = y+dy[i]
            nx = x+dx[i]
            if 0<=ny<H and 0<=nx<W and arr[ny][nx]:
                Q.append((ny, nx))


dy = [-1, 1, 0, 0, 1, 1, -1, -1]
dx = [0, 0, -1, 1, 1, -1, 1, -1]
while True:
    W, H = map(int, input().split())
    if W == 0 and H == 0:
        break
    arr = [list(map(int, input().split())) for _ in range(H)]
    result = 0
    Q = deque()
    for h in range(H):
        for w in range(W):
            if arr[h][w]:
                bfs(h, w)
                result += 1
    print(result)


# 아래는 재귀함수를 활용한 DFS로 풀었는데
# 메모리초과를 피하지 못했습니다ㅜㅜ
# 재귀를 계속 돌면서 함수 내 메모리를 전부 사용한 것 같은데...
# import sys
# sys.setrecursionlimit(10**9)


# def dfs(y, x): # 섬을 바다로 만들어 주면서 섬 개수 세기
#     if arr[y][x] == 0:
#         return
#     arr[y][x] = 0
#     for i in range(8):
#         ny = y+dy[i]
#         nx = x+dx[i]
#         if 0<=ny<H and 0<=nx<W and arr[ny][nx]:
#             dfs(ny, nx)


# dy = [-1, 1, 0, 0, 1, 1, -1, -1]
# dx = [0, 0, -1, 1, 1, -1, 1, -1]
# while True:
#     W, H = map(int, input().split())
#     if W == 0 and H == 0:
#         break
#     arr = [list(map(int, input().split())) for _ in range(H)]
#     result = 0
#     for h in range(H):
#         for w in range(W):
#             if arr[h][w]:
#                 dfs(h, w)
#                 result += 1
#     print(result)