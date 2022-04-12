N, A, B = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
# print(arr)
A, B = A-1, B-1
result = 'HAPPY'
for a in arr[A]:
    if a > arr[A][B]:
        result = 'ANGRY'
for i in range(N):
    if arr[i][B] > arr[A][B]:
        result = 'ANGRY'
print(result)