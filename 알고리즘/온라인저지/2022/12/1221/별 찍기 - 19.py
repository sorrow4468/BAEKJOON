def fill(arr):
    for k in range(0, size//2+1, 2):
        for i in range(k, size-k):
            arr[i][k] = 1

def rotate(arr):
    new_arr = []
    for j in range(size):
        tmp = []
        for i in range(size-1, -1, -1):
            tmp.append(arr[i][j])
        new_arr.append(tmp)
    return new_arr

N = int(input())
size = 1
for _ in range((N-1)*2): size += 2
arr = [[0]*size for _ in range(size)]
for _ in range(4):
    fill(arr)
    arr = rotate(arr)
for i in range(size):
    for j in range(size):
        if arr[i][j]:
            print('*', end='')
        else: print(' ', end='')
    if i != size-1: print()