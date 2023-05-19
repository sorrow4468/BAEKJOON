N = int(input())
A = '@'*N
B = ' '*N
S = A*3+B+A
M = A+B+A+B+A
E = A+B+A*3
for i in range(N):
    print(S)
for i in range(N*3):
    print(M)
for i in range(N):
    print(E)