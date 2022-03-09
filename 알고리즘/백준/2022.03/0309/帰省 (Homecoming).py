A, B, C = map(int, input().split())

result = 1

if C < A or C >= B:
    result = 0

print(result)