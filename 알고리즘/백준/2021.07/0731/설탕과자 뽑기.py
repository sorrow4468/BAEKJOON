h, w = map(int, input().split()) # 뽑기 상자의 가로 세로
n = int(input()) # 막대 개수
points = [] # 막대길이, 방향, 좌표 리스트
for i in range(n):
    l, d, x, y = map(int, input().split()) 
        # 막대 개수만큼 for문 돌리면서 정보 입력
    points.append([l, d, x, y])
        # 막대 길이, 막대 놓는 방향(0:가로, 1:세로), 막대 좌표x, 막대 좌표y(x, y = 1, 1 에서 시작)
board = [] # 빈 보드
for i in range(h):# 세로줄 만들면서
    board.append([])
    for j in range(w): # 가로에 전부 0 채우기
        board[i].append(0)

for point in points:
    if point[1] == 0: # 가로일 때
        for i in range(point[0]): # 막대 길이만큼
            board[point[2]-1][point[3]-1 + i] = 1
                # 오른쪽으로 1 넣어주기
    else: # 세로일 때
        for j in range(point[0]): # 막대 길이만큼
            board[point[2]-1 + j][point[3]-1] = 1
                # 아래로 1 넣어주기

for i in range(h):
  for j in range(w): 
    print(board[i][j], end=' ')
  print() # 출력문