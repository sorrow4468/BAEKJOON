for t in range(int(input())):
    N, M = map(int, input().split())
    U = M*2 - N
    T = M - U
    print(U, T)