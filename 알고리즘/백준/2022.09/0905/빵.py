result = int(1e9)
for _ in range(int(input())):
    A, B = map(int, input().split())
    if A <= B: result = min(result, B)
print(-1 if result == int(1e9) else result)