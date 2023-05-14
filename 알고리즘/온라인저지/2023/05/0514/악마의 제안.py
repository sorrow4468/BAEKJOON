K, N = map(int, input().split())
result = -1
if N != 1:
    A, B = N*K, N-1
    result = A//B
    if A%B: result += 1
print(result)