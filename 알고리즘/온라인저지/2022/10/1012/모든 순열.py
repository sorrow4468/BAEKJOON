def perm(arr, i):
    if i == len(arr)-1:
        result.append(arr[:])
    else:
        for j in range(i, len(arr)):
            arr[i], arr[j] = arr[j], arr[i]
            perm(arr, i+1)
            arr[i], arr[j] = arr[j], arr[i]

arr = list(range(1, int(input())+1))
result = []
perm(arr, 0)
result.sort()
for r in result: print(*r)