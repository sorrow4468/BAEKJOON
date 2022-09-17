def dfs(start):
    global is_dfs, result, visited
    print(start)
    if start == 1:
        for j in arr[1]:
            result = []
            visited = [True] + [False] * N            
            visited[start] = True
            result.append(start)
            dfs(j)
            tmp.append(result)
            if result == answer:
                is_dfs = True
    else:
        visited[start] = True
        result.append(start)
        for i in arr[start]:
            if not visited[i]:
                dfs(i)

N = int(input())
arr = [[] for _ in range(N+1)]
for n in range(N-1):
    s, e = map(int, input().split())
    arr[s].append(e)
    arr[e].append(s)
answer = list(map(int, input().split()))[::-1]
is_dfs = False
result = []
tmp = []
visited = [True] + [False] * N
tmp = []
dfs(1)
print(tmp)
if is_dfs:
    print(1)
else:
    print(0)
