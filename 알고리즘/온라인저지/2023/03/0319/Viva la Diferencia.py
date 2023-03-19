while True:
    A, B, C, D = map(int, input().split())
    if A == B == C == D == 0: break
    result = 0
    while not (A == B == C == D):
        A, B, C, D = map(abs, (A-B, B-C, C-D, D-A))
        result += 1
    print(result)