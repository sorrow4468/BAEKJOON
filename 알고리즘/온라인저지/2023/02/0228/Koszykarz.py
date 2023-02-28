K, W, M = map(int, input().split())
A = W-K
print(A//M+1 if A%M else A//M)