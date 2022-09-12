bracket = {
    ')': '(',
    '}': '{',
    ']': '[',
}

while True:
    sen = input() # sys.stdin.readline() 쓰니까 종료조건을 회피하지 못하더라
    if sen == '.':
        break
    stack = []
    for s in sen:
        if s in '[{(':
            stack.append(s)
        elif s in ')}]':
            if stack:
                if bracket[s] == stack[-1]:
                    stack.pop()
                else:
                    stack.append(s)
            else:
                stack.append(s)
    if stack:
        print('no')
    else:
        print('yes')
    