import sys
from collections import deque

input = sys.stdin.readline
dy, dx = [-1, 1, 0, 0], [0, 0, -1, 1]

def melt_check():
    global time
    melt = True
    for i in range(N):
        for j in range(M):
            if arr[i][j]:
                melt = False
    if not melt: time += 1
    return melt

def delta_move(y, x):
    for i in range(4):
        ny, nx = y+dy[i], x+dx[i]
        if 0<=ny<N and 0<=nx<M and not visited[ny][nx]:
            if arr[ny][nx]:
                cheese_Q.append((ny, nx))
                visited[ny][nx] = 2 # 방문 배열에 2는 치즈
                # 치즈를 녹일 때 주위에 1(공기)이 2개 이상 있으면 녹일 것
            else: 
                Q.append((ny, nx))
                visited[ny][nx] = 1 # 방문 배열에 1은 공기

def melt_cheese(y, x):
    tmp = 0
    for i in range(4):
        ny, nx = y+dy[i], x+dx[i]
        if visited[ny][nx] == 1: tmp += 1
    if tmp >= 2:
        melt_Q.append((y, x))
    else: visited[y][x] = 0
    # 치즈 배열의 특성상 반드시 두 면 이상 공기와 접촉하는 치즈가 있고
    # 녹은 치즈, 즉 새로운 탐색점은, 매 while문마다 반드시 나온다

N, M = map(int, input().rstrip().split())
arr = [list(map(int, input().rstrip().split())) for _ in range(N)]
Q, cheese_Q, melt_Q = deque(), deque(), deque()
visited = [[0]*M for _ in range(N)]
Q.append((0, 0))
visited[0][0] = 1
time = 0
while True:
    if melt_check(): print(time); break
    while Q: # 공기를 탐색하면서
        y, x = Q.popleft()
        delta_move(y, x) # 치즈를 찾자
    while cheese_Q: # 치즈들 중에서
        y, x = cheese_Q.popleft()
        melt_cheese(y, x) # 녹일 수 있는 치즈를 찾자
    while melt_Q: # 녹일 수 있는 치즈들을
        y, x = melt_Q.popleft()
        arr[y][x] = 0 # 녹이자
        visited[y][x] = 1
        Q.append((y, x))
    
"""
치즈가 녹은 자리는 공기가 된다
녹이고 Q에 추가하기
"""

# https://www.acmicpc.net/problem/2638