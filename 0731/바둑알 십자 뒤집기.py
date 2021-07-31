num = 19
board = [[int(x) for x in input().split()] for y in range(num)]

n = int(input())

points = []
for i in range(n): # 뒤집을 점들의 개수만큼
    a, b = map(int, input().split())
    points.append([a, b])
        # 입력 받아서 좌표들을 리스트로 저장
    
def cross(x, y): # 십자뒤집기 로직
    for i in range(19):
        if board[x-1][i] == 0: # 가로줄 0 -> 1, 1 -> 0
            board[x-1][i] = 1
        else:
            board[x-1][i] = 0
        if board[i][y-1] == 0: # 세로줄 0 -> 1, 1 -> 0
            board[i][y-1] = 1
        else:
            board[i][y-1] = 0
    return board

for point in points:
    cross(point[0], point[1]) # 좌표들 각각 십자뒤집기 실행

for i in range(19) :
  for j in range(19) : 
    print(board[i][j], end=' ')
  print() # 출력문