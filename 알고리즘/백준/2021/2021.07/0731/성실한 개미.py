num = 10
board = [[int(x) for x in input().split()] for y in range(num)]
    # 10 * 10 배열 받기
"""
스타트는 고정
개미가 있는 자리가 0이면 
    있는 자리를 9로 바꾸고
    그 오른쪽칸이 1이면 다음 경로를 한칸 아래로
    그 외에는 오른쪽으로
    2가 있는 자리에 도착할건데 만약 아닐수 있으니
    2인지 확인하고 9로 바꿔주고 코드 종료
"""
# 개미의 x, y좌표
# 인덱스에서는 [y][x]로 호출해야함
y = 1
x = 1
ant = board[y][x]

while board[y][x] == 0:
    board[y][x] = 9
    if board[y][x+1] == 1:
        y += 1
    elif board[y][x+1] == 0:
        x += 1
    elif board[y][x+1] == 2:
        x += 1
if board[y][x] == 2:
    board[y][x] = 9

for i in range(10):
  for j in range(10): 
    print(board[i][j], end=' ')
  print() # 출력문