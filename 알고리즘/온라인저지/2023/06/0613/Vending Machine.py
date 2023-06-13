result = 5000
for i in list(map(int, input().split())):
    if i == 1:
        result -= 500
    if i == 2:
        result -= 800
    if i == 3:
        result -= 1000
print(result)