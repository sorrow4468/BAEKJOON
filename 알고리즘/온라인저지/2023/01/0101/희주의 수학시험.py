A, B = map(int, input().split())
arr = [0]*(B+1)
k = 0
for i in range(1, B+1):
    for j in range(i):
        k += 1
        if k <= B:
            arr[k] = i
print(sum(arr[A:B+1]))