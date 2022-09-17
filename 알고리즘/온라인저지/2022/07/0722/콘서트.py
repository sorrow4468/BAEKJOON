N = int(input())
A = list(map(int, input().split())) # first sold
A.sort()
C = list(range(1, len(A)+1))
for i in range(len(A)):
    if A[i] != C[i]:
        print(C[i])
        exit()
print(N+1)