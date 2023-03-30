for _ in range(int(input())):
    N = int(input())
    for n in range(N):
        A, B = map(int, input().split())
        print(A+B, A*B)