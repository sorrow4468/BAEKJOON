R, C, W = map(int, input().split())
N = R+W-1
P = [[1], [1, 1], [1, 2, 1]]
for n in range(N-3):
    tmp = [0] * (2+n)
    for i in range(len(P[-1])-1):
        tmp[i] = sum(P[-1][i:i+2])
    tmp = [1]+tmp+[1]
    P.append(tmp)
result = 0
j = 0
for i in range(R-1, N):
    j += 1
    tmp = P[i][C-1:C+j-1]
    result += sum(tmp)
print(result)