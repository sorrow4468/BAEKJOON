N = int(input())
result = 0
for n in range(N, -1, -1):
    gms = True
    for s in str(n):
        if s not in '47':
            gms = False
    if gms:
        result = n
        break
print(result)