T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    result = M - (N-1)
    print(f'Case {t}: {result}')