import sys

N = int(sys.stdin.readline())

stack = []

for n in range(N):
    order = sys.stdin.readline().split()
    if order[0] == 'push':
        stack.append(order[1])
    elif order[0] == 'pop':
        if stack:
            tmp = stack.pop()
            print(tmp)
        else:
            print(-1)
    elif order[0] == 'size':
        print(len(stack))
    elif order[0] == 'empty':
        if stack:
            print(0)
        else:
            print(1)
    elif order[0] == 'top':
        if stack:
            print(stack[len(stack)-1])
        else:
            print(-1)
    