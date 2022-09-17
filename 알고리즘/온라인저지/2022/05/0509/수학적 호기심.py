for t in range(int(input())):
    N, M = map(int, input().split())
    result = 0
    for i in range(1, N-1):
        for j in range(i+1, N):
            # print((i**2 + j**2 + M)/(i*j))
            case1 = (i**2 + j**2 + M)/(i*j)
            case2 = (i**2 + j**2 + M)//(i*j)
            if case1 == case2:
                result += 1
    print(result)