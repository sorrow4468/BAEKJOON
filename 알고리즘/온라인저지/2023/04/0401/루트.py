while True:
    B, N = map(int, input().split())
    
    if B == 0 and N == 0: break

    minn = int(1e9)
    result = 0

    for A in range(1, int(1e9)):
        D = abs(B - A**N)

        if D < minn: 
            minn = D
            result = A
        else: break
    
    print(result)