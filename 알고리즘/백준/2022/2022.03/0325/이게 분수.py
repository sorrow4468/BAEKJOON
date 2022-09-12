import copy


def rotate():
    global arr
    new = []
    for j in range(2):
        tmp = []
        for i in range(1, -1, -1):
            tmp.append(arr[i][j])
        new.append(tmp)
    arr = copy.deepcopy(new)

arr = [list(map(int, input().split())) for _ in range(2)]
# print(arr)
maxx = 0
result = 0
# rotate()
for i in range(4):
    A, B, C, D = arr[0][0], arr[0][1], arr[1][0], arr[1][1]
    fraction = A/C + B/D
    if fraction > maxx:
        maxx = fraction
        result = i
    rotate()
print(result)