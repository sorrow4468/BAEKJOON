K = int(input())
stack = []
top = -1
for k in range(K):
    num = int(input())
    if num == 0:
        if top == -1:
            continue
        else:
            stack.pop()
            top -= 1
    else:
        stack.append(num)
        top += 1
print(sum(stack))