A, B = input().split()
result = [['.']*len(A) for _ in range(len(B))]
y = 0
char = ''
for a in A[::-1]:
    if a in B:
        y = B.index(a)
        char = a
x = A.index(char)
for j in range(len(A)): result[y][j] = A[j]
for i in range(len(B)): result[i][x] = B[i]
for i in range(len(result)):
    for j in range(len(result[i])):
        print(result[i][j], end='')
    if i < len(result)-1: print()