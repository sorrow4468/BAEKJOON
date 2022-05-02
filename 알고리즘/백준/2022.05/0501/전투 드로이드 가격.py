menu = [350.34, 230.90, 190.55, 125.30, 180.90]
for t in range(int(input())):
    tmp = list(map(int, input().split()))
    result = 0
    for i in range(5):
        result += menu[i]*tmp[i]
    print(f'${result:.2f}')