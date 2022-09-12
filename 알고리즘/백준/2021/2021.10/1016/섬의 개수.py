from collections import deque

dx = [-1, 1, 0, 0, -1, 1, -1, 1] # 8방향
dy = [0, 0, -1, 1, -1, -1, 1, 1]

while True: # 0 0 을 받을때까지
    w, h = map(int, input().split())
    if w+h == 0: # 종료조건
        break

    arr = [] # 섬과 육지

    for i in range(h):
        arr.append(list(map(int, input().split())))
    
    q = deque()
    cnt = 0 # 섬의 개수 초기화

    # 배열 전체를 확인하면서
    # 육지가 나오면, 그 육지를 바다로 바꿔버리고
    # 주변 8칸에 또 육지가 있는지 즉, 이어져 있는 섬인지 확인할 것
    for i in range(h):
        for j in range(w): # 배열을 돌면서
            if arr[i][j]: # 육지를 찾았다?
                q.append((j, i)) # 탐색할 육지에 추가
                
                while q: # 탐색할 육지가 있을 때
                    tmp = q.popleft() # 육지 좌표
                    a = tmp[0]
                    b = tmp[1]

                    if arr[b][a] == 0: # 가지치기 조건
                        # 탐색하려던 육지좌표였지만
                        # 다른 육지를 탐색하던 중 바다로 만들었다면
                        continue

                    arr[b][a] = 0 # 해당 육지를 바다로 만들어버리자

                    for k in range(8): # 8방향 BFS
                        nx = a+dx[k]
                        ny = b+dy[k]

                        if 0 <= nx < w and 0 <= ny < h and arr[ny][nx]:
                            # 범위를 벗어나지 않고, 8방향중 하나로 이동할 수 있는 육지면
                            # 즉 이어져 있는 섬이면
                            q.append((nx, ny)) # 탐색할 육지에 추가
                    
                cnt += 1 # while문을 통해 섬을 전부 바다로 만들었다
                # 해당 섬은 사라졌고, 우리는 섬이 하나 존재하였음을 확인할 수 있음

    print(cnt) # 확인된 섬의 개수