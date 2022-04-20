R, C, N = map(int, input().split())
A = R//N
B = C//N
if R%N:
    A += 1
if C%N:
    B += 1
print(A*B)