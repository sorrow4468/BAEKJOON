from collections import deque
import sys

input = sys.stdin.readline

R, C = map(int, input().split())
arr = []
for _ in range(R):
    tmp = list(input())
    arr.append(tmp)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
q = deque()
V = O = 0

for r in range(R): # 행
    for c in range(C): # 열
        if arr[r][c] in '.vo': # BFS
            q.append((r, c))
            v = o = 0
            while q:
                tmp = q.popleft()
                y, x = tmp[0], tmp[1]
                if arr[y][x] != '1':
                    if arr[y][x] == 'o':
                        o += 1
                    elif arr[y][x] == 'v':
                        v += 1
                arr[y][x] = '1'
                for i in range(4):
                    ny = y+dy[i]
                    nx = x+dx[i]
                    try:
                        if arr[ny][nx] in '.vo':
                            if arr[ny][nx] != '1':
                                if (ny, nx) not in q:
                                    q.append((ny, nx))
                    except:
                        q = deque()
                        v = o = 0
            # print(o, v) # 디버깅
            if o > v:
                O += o
            else:
                V += v

print(O, V)