def gcd(a, b):
    while b > 0:
        a, b = b, a%b
    return a

N = int(input())
GCD = 0
if N == 2:
    A, B = map(int, input().split())
    GCD = gcd(A, B)
else:
    A, B, C = map(int, input().split())
    GCD = gcd(gcd(A, B), gcd(B, C))
result = []
for i in range(1, int(GCD**0.5)+1):
    if GCD%i == 0:
        A, B = GCD//i, i
        if A != B:
            result.append(A)
            result.append(B)
        else:
            result.append(A)
for i in sorted(result):
    print(i)