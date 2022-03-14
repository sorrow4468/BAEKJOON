import sys
def input():
    return sys.stdin.readline()

N, M = map(int, input().split())

arr = []

tmp = list(map(int, input().split()))
num = 0
line = []
for t in tmp:
    num += t
    line.append(num)
arr.append(line)

for n in range(1, N):
    tmp = list(map(int, input().split()))
    num = 0
    line = []
    for t in tmp:
        num += t
        line.append(num)
    for i in range(len(line)):
        line[i] += arr[-1][i]
    arr.append(line)
    

for m in range(M):
    y1, x1, y2, x2 = (map(int, input().split()))
    e = v = h = s = 0
    if x1 > 1 and y1 > 1 and x2 > 1 and y2 > 1:
        e = arr[y2-1][x2-1]
        v = arr[y2-1][x1-2]
        h = arr[y1-2][x2-1]
        s = arr[y1-2][x1-2]
    elif x1 == 1 and y1 > 1:
        e = arr[y2-1][x2-1]
        h = arr[y1-2][x2-1]
    elif y1 == 1 and x1 > 1:
        e = arr[y2-1][x2-1]
        v = arr[y2-1][x1-2]
    elif x1 == 1 and y1 == 1:
        e = arr[y2-1][x2-1]

    result = e - v - h + s
    print(result)

# for a in arr:
#     print(*a)

"""
2 2 3 4 = [3][4]-[3][1]-[1][4]+[1][1]
"""