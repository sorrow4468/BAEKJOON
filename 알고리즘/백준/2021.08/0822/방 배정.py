N, K = map(int, input().split())
arr = [[0]*2 for _ in range(6)]
for n in range(N):
    S, Y = map(int, input().split())
    arr[Y-1][S] += 1
new_arr = []
for ar in arr:
    for a in ar:
        new_arr.append(a)
result = 0
for ar in new_arr:
    if ar > K:    
        result += ar//K
        ar = ar%K
    if not ar:
        continue
    else:
        result += 1
print(result)