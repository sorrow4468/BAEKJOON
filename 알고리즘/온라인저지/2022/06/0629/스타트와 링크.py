from itertools import combinations as comb

N = int(input())
scope = N
count = scope//2
tmp = list(comb(list(range(scope)), count))
result = 1e9
arr = [list(map(int, input().split())) for _ in range(N)]
for i in range(len(tmp)//2):
    start = tmp[i]
    link = tmp[-i-1]
    S = L = 0
    for j in range(N):
        for k in range(N):
            if j in start and k in start:
                S += arr[j][k]
            elif j in link and k in link:
                L += arr[j][k]
    if abs(S-L) < result:
        result = abs(S-L)
print(result)