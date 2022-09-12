arr = list(map(int, input().split()))
tmp = sorted(arr)
while arr != tmp:
    for i in range(len(arr)-1):
        if arr[i] > arr[i+1]:
            arr[i], arr[i+1] = arr[i+1], arr[i]
            print(*arr)