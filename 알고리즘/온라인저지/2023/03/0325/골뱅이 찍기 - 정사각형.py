N = int(input())
arr = []
A, B = '@'*(N+2), '@'+' '*N+'@'
arr.append(A)
for _ in range(N):
    arr.append(B)
arr.append(A)
for a in arr:
    print(a)