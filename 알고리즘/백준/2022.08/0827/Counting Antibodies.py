result = 0
for _ in range(2):
    tmp = 1
    for i in list(map(int, input().split())): tmp *= i
    result += tmp
for i in list(map(int, input().split())): result *= i
print(result)