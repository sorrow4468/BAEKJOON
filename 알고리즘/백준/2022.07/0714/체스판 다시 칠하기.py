def check_tile(y, x):
    cnt = 0
    switch = False # Black:True, White:False
    for i in range(8):
        for j in range(8):
            tmp = arr[y+i][x+j]
            switch = not switch
            if j == 0:
                switch = not switch
            if switch: # Black
                if tmp == 'W':
                    cnt += 1
            elif not switch: # White
                if tmp == 'B':
                    cnt += 1
    result = min(cnt, 64-cnt)
    return result


N, M = map(int, input().split())
arr = [list(input()) for _ in range(N)]
result = 1e9
for i in range(N-7):
    for j in range(M-7):
        tmp = check_tile(i, j)
        if tmp < result:
            result = tmp
print(result)