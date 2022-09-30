import sys

input = sys.stdin.readline

def cover(x1, y1, x2, y2):
    for i in range(y1, y2):
        for j in range(x1, x2):
            arr[i][j] += 1

def check():
    result = 0
    for i in range(100):
        for j in range(100):
            if arr[i][j]>M: result += 1
    return result

N, M = map(int, input().rstrip().split())
arr = [[0]*100 for _ in [0]*100]
for n in range(N):
    x1, y1, x2, y2 = map(int, input().rstrip().split())
    x1, y1 = x1-1, y1-1
    cover(x1, y1, x2, y2)
print(check())