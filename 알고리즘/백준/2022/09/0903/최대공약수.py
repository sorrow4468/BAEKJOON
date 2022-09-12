def gcd(a, b):
    while b > 0: a, b = b, a%b
    return a

A, B = map(int, input().split())
for _ in range(gcd(A, B)): print(1, end='')