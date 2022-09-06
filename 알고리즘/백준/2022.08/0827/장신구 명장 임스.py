P, N = map(int, input().split())
A = sorted(list(map(int, input().split()))) # accessories
result = 0
for a in A:
    if P >= 200: break
    P += a
    result += 1
print(result)