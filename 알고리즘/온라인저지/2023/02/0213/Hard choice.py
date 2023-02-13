A, B, C = map(int, input().split())
D, E, F = map(int, input().split())
result = 0
if A < D: result += D-A
if B < E: result += E-B
if C < F: result += F-C
print(result)