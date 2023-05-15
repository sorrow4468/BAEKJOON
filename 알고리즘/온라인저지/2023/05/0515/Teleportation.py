A, B, X, Y = map(int, input().split())
A, B = min((A, B)), max((A, B))
X, Y = min((X, Y)), max((X, Y))
result = 0
result += abs(A-X)
result += abs(B-Y)
result = min(result, abs(A-B))
print(result)
