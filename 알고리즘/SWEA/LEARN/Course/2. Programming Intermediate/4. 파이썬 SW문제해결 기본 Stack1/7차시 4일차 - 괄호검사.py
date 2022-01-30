T = int(input())

for t in range(1, T+1):
    code = input()
    
    stack = []
    bracket = ['(', ')', '{', '}']

    for c in code:
        if c == bracket[0]:
            stack.append(c)
        elif c == bracket[1]:
            if stack:
                if stack[-1] == bracket[0]:
                    stack.pop()
                else:
                    stack.append(c)
            else:
                stack.append(c)
        elif c == bracket[2]:
            stack.append(c)
        elif c == bracket[3]:
            if stack:
                if stack[-1] == bracket[2]:
                    stack.pop()
                else:
                    stack.append(c)
            else:
                stack.append(c)
    
    result = 0
    if stack:
        result = 0
    else:
        result = 1
    
    
    print('#{} {}'.format(t, result))
