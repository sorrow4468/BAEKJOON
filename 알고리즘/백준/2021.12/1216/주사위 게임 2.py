N = int(input())

A = B = 100

for n in range(N):
    a, b = map(int, input().split())

    if a > b:
        B -= a
    elif b > a:
        A -= b

print(A)
print(B)