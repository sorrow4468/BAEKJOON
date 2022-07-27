T = int(input())
for t in range(1, T+1):
    N = int(input())
    A = list(map(int, input().split())) # all prices
    result = []
    for i in range(N):
        tmp = A.pop(0)
        O = (tmp//3) * 4 # original
        for j in range(len(A)):
            if A[j] == O:
                A.pop(j)
                break
        result.append(tmp)
    print(f'Case #{t}:', *result)