N = int(input())
result = 0
if N == 1:
    print(result)
else:
    D = int(input()) # dasom
    C = [int(input()) for _ in range(N-1)]
    while D <= max(C):
        C.sort(reverse=True)
        D += 1
        result += 1
        C[0] -= 1
    print(result)