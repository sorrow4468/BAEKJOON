result = 0
for _ in range(int(input())):
    gifticon = input().split('D-')
    left_day = int(gifticon[1])
    if left_day <= 90:
        result += 1
print(result)