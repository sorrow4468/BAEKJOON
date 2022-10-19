N, M = map(int, input().split())
ants1 = list(input())
ants2 = list(input())
T = int(input())
arr = []
for i in range(N): arr.append((ants1[::-1][i], 1))
for i in range(M): arr.append((ants2[i], -1))
time = 0
while time < T:
    time += 1
    i = 0
    while i < N+M-1:
        ant1, ant2 = arr[i], arr[i+1]
        if ant1[1] == 1 and ant2[1] == -1:
            arr[i], arr[i+1] = arr[i+1], arr[i]
            i += 1
        i += 1
result = ''
for a in arr: result += a[0]
print(result)