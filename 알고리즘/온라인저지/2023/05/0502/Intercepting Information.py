result = 'S'
for i in list(map(int, input().split())):
    if i not in (0, 1):
        result = 'F'
print(result)