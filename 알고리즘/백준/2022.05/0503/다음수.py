while True:
    A, B, C = map(int, input().split())
    if A == B == C == 0:
        break
    result = 'AP'
    if B-A == C-B: # AP
        print(result, C + (C-B))
    else: # GP
        result = 'GP'
        print(result, (C * (B//A)))