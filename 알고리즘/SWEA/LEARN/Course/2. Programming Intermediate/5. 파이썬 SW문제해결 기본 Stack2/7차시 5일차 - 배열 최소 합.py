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


"""
2022-09-01에 다시 풀음
def dfs(level):
    global result, tmp
    if level == N:
        result = min(result, tmp)
        return
    if tmp > result: return
    for i in range(N):  
        # print(level, i, arr[level][i])
        if not visited[i]:
            tmp += arr[level][i]
            visited[i] = 1
            dfs(level+1)
            tmp -= arr[level][i]
            visited[i] = 0

for t in range(1, int(input())+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    # for a in arr: print(a)
    visited = [0] * N
    result = int(1e9)
    tmp = 0
    dfs(0)
    print('#{} {}'.format(t, result))
"""