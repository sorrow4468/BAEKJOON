T = int(input())
for t in range(T):
    result = 0
    tmp = input().split()
    for i in tmp:
        if i[0] == '-':
            result -= int(i[1:])
        else:
            result += int(i)
    print(result)