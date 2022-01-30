T = int(input())

for tc in range(T):
    a = input().split()
    b = float(a[0])

    for i in range(1, len(a)):
        if a[i] == '@':
            b *= 3
        elif a[i] == '%':
            b += 5
        elif a[i] == '#':
            b -= 7
    
    print('{:.2f}'.format(b))
