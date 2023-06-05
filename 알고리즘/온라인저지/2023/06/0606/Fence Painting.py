A, B = map(int, input().split())
C, D = map(int, input().split())
wall = [0]*101
for i in range(A, B): wall[i] = 1
for i in range(C, D): wall[i] = 1
print(sum(wall))