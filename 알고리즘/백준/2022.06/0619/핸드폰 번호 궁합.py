A = input()
B = input()
tmp1 = ''
tmp2 = ''
for i in range(8):
    tmp1 = tmp1 + A[i] + B[i]
for j in range(16, 2, -1):
    for i in range(1, j):
        tmp2 = tmp2 + str((int(tmp1[i-1]) + int(tmp1[i]))%10)
    tmp1, tmp2 = tmp2, ''
print(tmp1)