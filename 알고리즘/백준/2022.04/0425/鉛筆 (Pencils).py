N, A, B, C, D = map(int, input().split())
E = F = 0
if N%A:
    E = N//A + 1
else:
    E = N//A
if N%C:
    F = N//C + 1
else:
    F = N//C
# print(E, F)
print(min(E*B, F*D))