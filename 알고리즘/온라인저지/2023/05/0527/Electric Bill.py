A, B = map(int, input().split())
N = int(input())
for i in range(N):
    C = int(input())
    print(C, end=' ')
    result = 0
    if C > 1000:
        result += A*1000
        C -= 1000
        result += B*C
    else:
        result = A*C
    print(result)