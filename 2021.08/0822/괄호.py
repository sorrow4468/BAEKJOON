T = int(input())
for tc in range(T):
    data = input()
    stack = []
    top = -1
    for dt in data:
        if dt == '(':
            stack.append(dt)
            top += 1
        else: # dt == ')'
            if top == -1:
                stack.append(dt)
                break
            else:
                if stack[top] == '(':
                    stack.pop()
                    top -= 1
                else:
                    stack.append(dt)
                    break
    if stack:
        print('NO')
    else:
        print('YES')