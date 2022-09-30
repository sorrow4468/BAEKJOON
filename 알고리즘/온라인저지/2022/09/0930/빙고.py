import sys

input = sys.stdin.readline
cross = [
    (0, 0), (1, 1), (3, 3), (4, 4),
    (2, 2), 
    (4, 0), (3, 1), (1, 3), (0, 4),
    ]

def check(call):
    bingo = 0
    y, x = arr_dict[call]
    arr[y][x] = 1
    for i in range(5): # ga-ro
        is_bingo = True
        for j in range(5):
            if not arr[i][j]: is_bingo = False
        if is_bingo: bingo += 1

    for j in range(5): # se-ro
        is_bingo = True
        for i in range(5):
            if not arr[i][j]: is_bingo = False
        if is_bingo: bingo += 1

    is_bingo = True # dae-gak-seon 1
    for c in cross[:5]:
        i, j = c
        if not arr[i][j]: is_bingo = False
    if is_bingo: bingo += 1

    is_bingo = True # dae-gak-seon 2
    for c in cross[4:]:
        i, j = c
        if not arr[i][j]: is_bingo = False
    if is_bingo: bingo += 1
    if bingo>=3: return True

arr_dict = dict()
for i in range(5):
    nums = list(map(int, input().rstrip().split()))
    for j in range(5): arr_dict[nums[j]] = (i, j)
result = 0
arr = [[0]*5 for _ in range(5)]
flag = False
for i in range(5):
    calls = list(map(int, input().rstrip().split()))
    if flag: continue
    for call in calls:
        if flag: continue
        result += 1
        if check(call): flag = True
print(result)