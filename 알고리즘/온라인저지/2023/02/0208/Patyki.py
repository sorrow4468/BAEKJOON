A, B, C = sorted(list(map(int, input().split())))
result = 0
if A == B == C: result = 2
elif C**2 == A**2 + B**2: result = 1
print(result)