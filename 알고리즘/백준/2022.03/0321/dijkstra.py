def dijkstra():
    global result
    pass


N, D = map(int, input().split())
rodes = []
for n in range(N):
    tmp = list(map(int, input().split()))
    if tmp[1] > D:
        continue
    rodes.append(tmp)
rodes.sort(key=lambda x:x[0])
print(rodes)
result = D




print(result)