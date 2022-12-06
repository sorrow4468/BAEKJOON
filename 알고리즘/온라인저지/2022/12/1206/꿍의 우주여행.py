for _ in range(int(input())):
    N, D = map(int, input().split())
    result = 0
    for n in range(N):
        v, f, s = map(int, input().split())
        result += v*f >= D*s
    print(result)