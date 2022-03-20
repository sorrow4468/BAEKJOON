T = int(input())
teas = list(map(int, input().split()))
result = 0
for tea in teas:
    if T == tea:
        result += 1
print(result)