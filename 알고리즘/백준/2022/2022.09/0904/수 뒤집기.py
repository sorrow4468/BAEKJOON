for _ in range(int(input())):
    num = input()
    A, B = int(num), int(num[::-1])
    tmp = str(A+B)
    print('YES' if tmp == tmp[::-1] else 'NO')