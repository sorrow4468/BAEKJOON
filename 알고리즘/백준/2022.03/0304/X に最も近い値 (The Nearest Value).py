X, L, R = map(int, input().split())

result = 0

if X < L:
    result = L
elif L <= X < R:
    result = X
elif X >= R:
    result = R

print(result)