from collections import deque
from copy import deepcopy


def bfs(arr, y, x):
    pass


N = int(input())
normal_arr = [list(input()) for _ in range(N)]
CB_arr = deepcopy(normal_arr)
# for a in normal_arr: print(a)
for i in range(N): # 적록색약 배열
    for j in range(N):
        if CB_arr[i][j] in 'RG':
            CB_arr[i][j] = 'A'
# for c in CB_arr: print(c)
for i in range(N): # normal
    for j in range(N):
        if normal_arr[i][j]:
            pass
normal = 0
CB = 0 # color blind
print(normal, CB)