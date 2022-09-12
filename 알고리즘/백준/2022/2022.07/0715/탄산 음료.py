E, F, C = map(int, input().split()) # empty find change
result = 0
bottle = E+F
while bottle >= C:
    result += 1
    bottle -= C
    bottle += 1
print(result)