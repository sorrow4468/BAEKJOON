A, B, C = map(int, input().split())
result = 0
day = 0
coin = 0
while True:
    coin += A
    day += 1
    result += 1
    if day == 7:
        day = 0
        coin += B
    if coin >= C:
        break
print(result)