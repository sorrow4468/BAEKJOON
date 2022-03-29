while True:
    N = list(input())
    if N == ['0']:
        break
    else:
        result = 1
        for n in N:
            if n == '1':
                result += 3
            elif n == '0':
                result += 5
            else:
                result += 4
        print(result)