def down():
    global result
    for i in range(N-2, -1, -1):
        for j in range(M):
            if arr[i][j] == 1 and arr[i+1][j] == 0:
                arr[i][j], arr[i+1][j] = arr[i+1][j], arr[i][j]
                result += 1

T = int(input())
for t in range(T):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    result = 0
    for n in range(N-1):
        down()    
    print(result)