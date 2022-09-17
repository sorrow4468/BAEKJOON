def gcd(a, b):
    while b > 0: a, b = b, a%b
    return a

A, B = map(int, input().split())
C, D = map(int, input().split())
GCD = gcd(B, D)
LCM = GCD * (B//GCD) * (D//GCD)
E = A*(LCM//B) + C*(LCM//D)
F = LCM
GCD = gcd(E, F)
print(E//GCD, F//GCD)