N = int(input())
arr = list(map(int, input().split()))
# print(arr)
for i in range(N):
    arr[i] *= i+1
# print(arr)
if N > 0:
    for i in range(1, N):
        arr[i] -= sum(arr[:i])
print(*arr)