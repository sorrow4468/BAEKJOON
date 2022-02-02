N, M = map(int, input().split())

arr = []

for n in range(N):
    arr.append(list(map(int, input().split())))

K = int(input())

for k in range(K):
    i, j, x, y = map(int, input().split())

    summ = 0

    for a in range(i-1, x):
        for b in range(j-1, y):
            summ += arr[a][b]
    
    print(summ)

