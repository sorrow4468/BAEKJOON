def gcd(a, b):
    while b > 0: a, b = b, a%b
    return a

A, B = map(int, input().split())
GCD = gcd(A, B)
print(GCD * (A//GCD) * (B//GCD))