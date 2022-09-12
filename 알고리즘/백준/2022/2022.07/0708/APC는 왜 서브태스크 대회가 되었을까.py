N, L, K = map(int, input().split())
P = [] # problems
for n in range(N):
    P.append(tuple(map(int, input().split())))
P.sort(key=lambda x:x[1])
# print(P)
solved = [0] * N
k = 0
result = 0
for i in range(N):
    if k < K:
        if P[i][1] <= L:
            k += 1
            result += 140
        elif P[i][0] <= L:
            k += 1
            result += 100
print(result)
