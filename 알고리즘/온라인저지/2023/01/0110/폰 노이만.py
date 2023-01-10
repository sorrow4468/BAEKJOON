for _ in range(int(input())):
    N, D, A, B, F = map(float, input().split())
    print(int(N), f'{D/(A+B)*F:.6f}')