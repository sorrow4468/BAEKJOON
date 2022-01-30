from collections import deque # popleft() 사용할 것

dx = (-1, 1, 0, 0) # 델타이동 속도를 조금이라도 높이기 위해
dy = (0, 0, -1, 1) # tuple() 사용

N, M = map(int, input().split())

arr = []

for n in range(N):
    arr.append(list(map(int,input()))) # 공백 없으니, split()없이

q = deque()

q.append((0, 0, 1)) # 출발지점, 출발점부터 거리 카운트함

result = 0 # 결과값 초기화

while q: # == BFS
    tmp = q.popleft() # == pop(0)
    x = tmp[0] # 탐색할 x좌표
    y = tmp[1] # 탐색할 y좌표
    cnt = tmp[2] # 여기까지 오는데 걸린 거리
    if arr[y][x] == 0: # 이전 탐색에서 q에 담았었지만 꺼내보니 방문한 적이 있다면
        # 방문할 곳에 해당하여 q에 담았지만, 막상 차례가 되서 꺼내보니 탐색할 필요가 없다면
        # 아래 과정들을 또 진행하여 중복방문이 일어나지 않도록
        continue
    arr[y][x] = 0 # 방문처리
    # 처음에는 arr과 동일한 크기의 visited 배열을 만들어서 방문처리를 하였으나
    # 메모리가 넉넉하지 않은 문제임을 확인하였고
    # 원본 배열 자체에서 방문처리 하였음

    if x == M-1 and y == N-1: # 도착좌표
        result = cnt # 거리를 결과값에 저장
        break # 종료

    for i in range(4): # 탐색중인 좌표가 목적지가 아니라면 
        # 범위를 벗어나지 않고 방문한 적이 없는 주변 4칸 담을 것
        nx = x+dx[i] # 좌우
        ny = y+dy[i] # 상하
        if 0 <= nx < M and 0 <= ny < N and arr[ny][nx]:
            # 배열 안에서, 방문한 적이 없다면
            q.append((nx, ny, cnt+1)) # 방문할 곳에 추가

print(result)