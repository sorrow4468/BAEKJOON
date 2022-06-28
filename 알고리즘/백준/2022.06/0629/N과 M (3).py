def comb(scope, depth):
    for i in range(1, scope+1):
        result.append(i)
        if depth == M:
            print(*result)
        else:
            comb(scope, depth+1)
        result.pop()

N, M = map(int, input().split())
result = []
comb(N, 1)