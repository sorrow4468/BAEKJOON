N, D = map(int, input().split())
count = [0]*10
for i in range(1, N+1):
    for j in str(i):
        count[int(j)] += 1
print(count[D])