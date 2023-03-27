for _ in range(int(input())):
    D, N, S, P = map(int, input().split())
    A, B = D+N*P, N*S
    result = 'does not matter'
    if A<B: result = 'parallelize'
    if A>B: result = 'do not parallelize'
    print(result)