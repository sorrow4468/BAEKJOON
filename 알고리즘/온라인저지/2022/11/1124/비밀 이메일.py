import sys

input = sys.stdin.readline

message = input().rstrip()
length = len(message)
divs = []
for i in range(1, int((length+1)**0.5)+1):
    if not length%i:
        divs.append((i, length//i))
R, C = divs[-1]
arr = [[0]*C for _ in range(R)]
k = 0
for j in range(C):
    for i in range(R):
        arr[i][j] = message[k]
        k += 1
for i in range(R):
    for j in range(C):
        print(arr[i][j], end='')