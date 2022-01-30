def dfs(N, depth, tmp):
    global result
    if N == depth :
        if tmp < result:
            result = tmp
 
    if tmp > result:
        return
    else:
        for i in range(N):
            if visited[i] == 0:
                visited[i] = 1
                dfs(N, depth+1, tmp+arr[depth][i])
                visited[i] = 0
 
T = int(input())
for t in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [0]*N
 
    depth = 0
    result = 10*N
 
    dfs(N, 0, 0)
    print('#{} {}'.format(t, result))
