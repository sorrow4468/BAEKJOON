for t in range(int(input())):
    N, M = map(int, input().split())
    result = 0
    for a in range(N, M+1):
        for b in str(a):
            if b == '0':
                result += 1
    print(result)