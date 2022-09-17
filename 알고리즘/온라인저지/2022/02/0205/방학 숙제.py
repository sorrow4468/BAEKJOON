L = int(input())
A = int(input())
B = int(input())
C = int(input())
D = int(input())

maxx = 0

A_by_C = 0
if A%C == 0:
    A_by_C = A//C
else:
    A_by_C = A//C + 1

B_by_D = 0
if B%D == 0:
    B_by_D = B//D
else:
    B_by_D = B//D + 1

maxx = max(A_by_C, B_by_D)

print(L - maxx)