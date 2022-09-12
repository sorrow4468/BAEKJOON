N = int(input())

arr = list(map(int, input().split()))

start = arr[0]

up = True

maxx = 0

for i in range(1, N):
    if arr[i] <= arr[i-1]:
        up = False
        tmp = arr[i-1] - start
        start = arr[i]
        
        if tmp > maxx:
            maxx = tmp

    else:
        up = True

if up:
    if arr[i]-start > maxx:
        maxx = arr[i]-start
        
print(maxx)