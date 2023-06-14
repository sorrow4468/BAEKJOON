X = int(input())
Y = int(input())
result = []
while X<=Y:
    result.append(X)
    X += 60
for r in result:
    print(f'All positions change in year {r}')