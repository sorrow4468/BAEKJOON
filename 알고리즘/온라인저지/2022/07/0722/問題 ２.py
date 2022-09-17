N = int(input())
C = dict() # change
for n in range(N):
    a, b = input().split()
    C[a] = b
# print(C)
M = int(input())
for m in range(M):
    tmp = input()
    try:
        print(C[tmp], end='')
    except:
        print(tmp, end='')