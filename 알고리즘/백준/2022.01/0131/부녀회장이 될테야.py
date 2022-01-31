T = int(input())

ks = []
ns = []

for t in range(T):
    ks.append(int(input()))
    ns.append(int(input()))

maxk = max(ks)
maxn = max(ns)

a = [[0]*maxn for _ in range(maxk+1)]

a[0] = list(range(1, maxn+1))

for i in range(maxk+1):
    a[i][0] = 1

for i in range(1, maxk+1):
    for j in range(1, maxn):
        a[i][j] = a[i][j-1] + a[i-1][j]

for t in range(T):
    print(a[ks[t]][ns[t]-1])