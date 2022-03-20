N, D = map(int, input().split())
rodes = []
for n in range(N):
    tmp = list(map(int, input().split()))
    if tmp[2] > D:
        continue
    rodes.append(tmp)
print(rodes)