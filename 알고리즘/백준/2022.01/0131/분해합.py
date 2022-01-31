N = int(input())

if N == 1:
    print(0)
else:
    t = 0
    if N >= 100:
        t = len(str(N)) * 10
        M = N - t
    else:
        M = 1

    while True:
        M += 1

        a = 0

        for i in str(M):
            a += int(i)
        
        temp = M + a

        if temp == N:
            print(M)
            break
        elif M == N:
            print(0)
            break

