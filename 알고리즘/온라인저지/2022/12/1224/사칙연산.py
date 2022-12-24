for _ in range(int(input())):
    A, ope, B, equal, answer = input().split()
    A, B, answer = map(int, [A, B, answer])
    if ope == '+':
        result = A+B
    elif ope == '-':
        result = A-B
    elif ope == '*':
        result = A*B
    elif ope == '/':
        result = A//B
    print('correct' if result == answer else 'wrong answer')