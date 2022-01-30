T = int(input())

for t in range(1, T+1):
    arr = [[0]*10 for _ in range(10)]
    N = int(input())
    for n in range(N):
        tmp = list(map(int, input().split()))
        r1 = tmp[0]
        c1 = tmp[1]
        r2 = tmp[2]
        c2 = tmp[3]
        
        for i in range(c1, c2+1):
            for j in range(r1, r2+1):
                if tmp[4] == 1:
                    if arr[i][j] == 0:
                        arr[i][j] = 1
                    elif arr[i][j] == 2:
                        arr[i][j] = 3
                else:
                    if arr[i][j] == 0:
                        arr[i][j] = 2
                    elif arr[i][j] == 1:
                        arr[i][j] = 3
    
    cnt = 0
    for a in arr:
        cnt += a.count(3)
    print('#{} {}'.format(t, cnt))