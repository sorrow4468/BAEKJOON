TC = int(input())

for tc in range(1, TC+1):
    N = int(input())
    nodes = list(map(int, input().split()))
    arr = [0]

    for n in nodes:
        arr.append(n)

        for i in range(1, N//2+1):
            try:
                if arr[i] > arr[i*2]:
                    arr[i], arr[i*2] = arr[i*2], arr[i]    

                if arr[i] > arr[i*2+1]:
                    arr[i], arr[i*2+1] = arr[i*2+1], arr[i]
            
            except:
                pass

    n = len(arr)
    result = 0
    
    while True:
        N //= 2

        result += arr[N]

        if N == 1:
            break
            
    print('#{} {}'.format(tc, result))