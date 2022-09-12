while True:
    a, b = map(int, input().split())

    if a == 0 and b == 0:
        break

    result = 'neither'

    if a % b == 0:
        result = 'multiple'
    elif b % a == 0:
        result = 'factor'
    
    print(result)