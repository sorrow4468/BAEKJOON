N = int(input())

wnhs = []

result = []

for n in range(N):
    wnhs.append(tuple(map(int, input().split())))

for i in range(N):
    cnt = 1

    for j in range(N):
        if i != j and wnhs[i][0] < wnhs[j][0] and wnhs[i][1] < wnhs[j][1]:
            cnt += 1

    result.append(cnt)

print(*result)

