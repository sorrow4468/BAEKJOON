N, K = map(int, input().split())
P = [[1], [1, 1], [1, 2, 1]]
for n in range(N-3):
    tmp = [0] * (2+n)
    for i in range(len(P[-1])-1):
        tmp[i] = sum(P[-1][i:i+2])
    tmp = [1]+tmp+[1]
    P.append(tmp)
print(P[-1][K-1])