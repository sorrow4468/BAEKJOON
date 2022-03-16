from pprint import pprint

N, M, K = map(int, input().split())
arr = [[] for _ in range(N)]
for m in range(M):
    arr[m].append(True)
for m in range(M, N):
    arr[m].append(False)
# print(arr)
for k in range(K):
    arr[k].append(True)
for k in range(K, N):
    arr[k].append(False)
# pprint(arr)
result = N
for a in arr:
    if a[0] != a[1]:
        result -= 1
print(result)