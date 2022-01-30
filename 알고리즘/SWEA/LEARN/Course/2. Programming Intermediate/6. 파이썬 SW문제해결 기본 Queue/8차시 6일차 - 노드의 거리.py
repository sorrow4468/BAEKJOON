T = int(input())

for t in range(1, T+1):
    V, E = map(int, input().split())
    
    arr = [[] for _ in range(V+1)]

    for e in range(E):
        a, b = map(int, input().split())
        arr[a].append(b)
        arr[b].append(a)
    
    S, G = map(int, input().split())

    visited = [0] * (V+1)
    cnt = 0

    q = [arr[S]+[cnt]]
    visited[S] = 1
    result = 0
    found = False

    while q:
        tmp = q.pop(0)
        cnt = tmp[-1]
        if found:
            break

        for i in range(len(tmp)-1):
            if tmp[i] == G:
                result = cnt+1
                found = True
                break

            if visited[tmp[i]] == 0:
                q.append(arr[tmp[i]]+[cnt+1])
                visited[tmp[i]] = 1

    if S == G:
        result = 0

    print('#{} {}'.format(t, result))