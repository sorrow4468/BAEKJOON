result = 0
while True:
    order = input()
    if order == '=':
        print(result)
        break
    elif order in '+-*/':
        num = int(input())
        if order == '+':
            result += num
        elif order == '-':
            result -= num
        elif order == '*':
            result *= num
        elif order == '/':
            result //= num
    else:
        result = int(order)