# 상우하좌

dy = (-1, 0, 1, 0)
dx = (0, 1, 0, -1)

"""
N이 홀수일때 짝수일때 각각 스타트포인트 잡아서
델타 이동으로 배열을 채우면서
K의 좌표를 찾아서 저장 후
배열 다 채우고 배열 출력
K의 좌표 출력
"""

N = int(input())
K = int(input())

start_x = start_y = N//2

arr = [[0] * N for _ in range(N)]

arr[start_y][start_x] = 1

dir = 0
a = b = 0

for i in range(2, N**2 + 1):
    start_x = start_x + dx[dir]
    start_y = start_y + dy[dir]

    arr[start_y][start_x] = i
    if i == K:
        a = start_y
        b = start_x

    tp_x = start_x + dx[(dir+1)%4]
    tp_y = start_y + dy[(dir+1)%4]
    if not arr[tp_y][tp_x]:
        dir = (dir+1)%4

for ar in arr:
    print(*ar)
print(a+1, b+1) 