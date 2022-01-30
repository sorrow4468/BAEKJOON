# 모든 0에 벽을 세 개 세워보고 가장 안전영역을 많이 확보가능한게 정답
import copy # 2차원 배열 복사를 위한 import copy, deepcopy를 사용함
from collections import deque # bfs로 바이러스를 퍼뜨릴 때 사용할 deque

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

res = 0 # 결과값 초기화

def virus(): # 바이러스가 퍼진다!
    global res # 함수 밖에 있는 전역변수 res를 사용

    tmp = copy.deepcopy(arr) # 입력받은 배열 arr을 완전히 복제할 것
    # 벽을 세우고 허물고 할건데
    # 매번 세우는 벽의 위치가 바뀌는데 원본 배열을 들고 수정하기보다
    # 배열을 복사해서 백업을 따놓고 
    # "여기여기 벽을 세운거로는 바이러스를 못막는구나"는 결과가 확인이 되면
    # 해당 복사는 지우고 다시 원본 배열을 복사해서 또 벽을 세우고
    # 그 벽에 바이러스 퍼뜨려보고를 반복
    # 그런데 2차원 배열을 복사해야 하기 때문에 deepcopy를 사용함

    for i in range(N): # 바이러스 시작점을
        for j in range(M): # 찾자
            if tmp[i][j] == 2: # 해당 칸이 바이러스면
                q.append([i, j]) # 이동할 칸에 추가
                # 배열의 처음 바이러스 위치를 q에 담음
                # 이후 아래 while문을 반복하면서 바이러스를 퍼뜨림
    
    while q: # 바이러스가 퍼질 곳이 남아있다면
        x, y = q.popleft() # 맨 앞에 좌표부터 꺼내서
        for i in range(4): # 상하좌우 전부 확인
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M: # 연구소를 벗어나지 않는 범위에서
                if tmp[nx][ny] == 0: # 바이러스를 퍼뜨릴 수 있으면
                    tmp[nx][ny] = 2 # 받아라 바이러스!
                    q.append([nx,ny]) # 해당 좌표의 상하좌우에 또 바이러스가 퍼지도록 q에 담기

    cnt = 0 # 지금 세워진 벽에 대하여 바이러스가 얼마나 퍼졌는지 확인하는 변수 초기화
    
    for t in tmp:
        cnt += t.count(0) # 연구소 해당 줄에서 확인된 안전구역의 수
    
    res = max(res, cnt) # 전역변수 res와 비교하여 지금 세워진 벽에서의 안전구역이 더 많은지 비교하고 저장
    # if cnt > res: 와 같은 문장을 max()를 사용하였음

def wall(x):
    if x == 3: # 벽을 세 개 세웠다면
        virus() # 바이러스를 퍼뜨려보자!
        return # 바이러스를 다 퍼뜨리고 해당 재귀함수 종료, 다시 다른 벽을 세워보자
    
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 0: # 벽을 세울 수 있으면
                arr[i][j] = 1 # 벽을 세우고
                wall(x+1) # 다음 벽을 세우자
                arr[i][j] = 0 # 다른 위치에 벽을 세울 수 있도록 위에서 세웠던 벽을 허물자


N, M = map(int, input().split()) # 연구소의 가로와 세로 크기

arr = [list(map(int, input().split())) for _ in range(N)] # 연구소 상황

q = deque() # 바이러스를 퍼뜨릴 q

wall(0) # 벽 0개, 벽 1개, 벽 2개, 벽 3개, 그 시작은 0개

print(res) # 3개의 벽을 세운 각각의 경우에 대하여 얻은 안전구역의 수가 
# 기존에 얻은 안전구역의 수 보다 클 때마다 갱신해주어서
# 결국 벽을 세우는 모든 경우의 수에서 퍼뜨려 본 바이러스에 대해 확인된 안전구역의 최대 수가 담겨있는
# res를 출력