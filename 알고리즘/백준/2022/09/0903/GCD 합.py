def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a

for _ in range(int(input())):
    N = list(map(int, input().split()))
    n = N.pop(0)
    result = 0
    for i in range(n-1):
        for j in range(i+1, n):
            A, B = N[i], N[j]
            result += gcd(A, B)
    print(result)