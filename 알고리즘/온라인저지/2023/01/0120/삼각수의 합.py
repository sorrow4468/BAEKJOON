for _ in range(int(input())):
    N = int(input())
    result = 0
    for k in range(1, N+1):
        result += k*sum(list(range(1, k+2)))
    print(result)