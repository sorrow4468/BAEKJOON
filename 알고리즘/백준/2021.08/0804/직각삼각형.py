a, b, c = 1, 1, 1
result = []
while a + b + c != 0:
    a, b, c = map(int, input().split())
    if a + b + c == 0:
        continue
    if a**2 + b**2 == c**2:
        result.append('right')
    else:
        result.append('wrong')
for res in result:
    print(res)
