N = int(input())
arr = sorted(list(map(int, input().split())))
last_plus_1 = 0
result = 0
for a in arr:
    if a != last_plus_1:
        result += a
    last_plus_1 = a+1
print(result)