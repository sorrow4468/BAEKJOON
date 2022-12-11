while True:
    N = int(input())
    if N == 0: break
    while N >= 10:
        tmp = 0
        for n in str(N):
            tmp += int(n)
        N = tmp
    print(N)