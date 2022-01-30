T = int(input())

for t in range(1, T+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    tmp = M%N
    for i in range(tmp):
        arr.append(arr.pop(0))
    
    result = arr[0]

    print('#{} {}'.format(t, result))