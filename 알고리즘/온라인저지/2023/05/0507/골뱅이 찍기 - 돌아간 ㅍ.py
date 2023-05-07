def new_print(line):
    for _ in range(N):
        print(line)

N = int(input())
A = '@'*N + ' '*3*N + '@'*N
B = '@'*N*5
new_print(A)
new_print(B)
new_print(A)
new_print(B)
new_print(A)