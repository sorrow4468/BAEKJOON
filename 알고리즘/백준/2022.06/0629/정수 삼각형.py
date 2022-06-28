N = int(input())
arr = []
for n in range(N):
    tmp = [0] + list(map(int, input().split())) + [0]
    arr.append(tmp)
for i in range(1, len(arr)):
    for j in range(1, len(arr[i])-1):
        tmp = arr[i-1][j-1:j+1]
        arr[i][j] += max(tmp)
print(max(arr[N-1]))