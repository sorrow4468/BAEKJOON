result = 0
for i in list(input().split()):
    if i[0] not in ('-', '0'):
        result += 1
print(result)