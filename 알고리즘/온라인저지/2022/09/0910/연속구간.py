for _ in range(3):
    num = input()
    prev = num[0]
    tmp = 1
    result = 1
    for i in range(1, 8):
        if prev == num[i]:
            tmp += 1
        else:
            result = max(result, tmp)
            tmp = 1
            prev = num[i]
    print(max(result, tmp))