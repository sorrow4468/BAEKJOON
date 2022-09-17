N = int(input())
result = 0
for b in range(1, 501):
    for a in range(1, 501):
        if a**2 == b**2 + N:
            result += 1
print(result)