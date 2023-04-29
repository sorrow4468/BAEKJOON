A, B = '', ''
N = int(input())
B = '@'*N*5
A = '@'*N+' '*N*3+'@'*N
for _ in range(N*2):
    print(A)
for _ in range(N):
    print(B)
for _ in range(N):
    print(A)
for _ in range(N):
    print(B)

"""
N*2
N
N
N
"""