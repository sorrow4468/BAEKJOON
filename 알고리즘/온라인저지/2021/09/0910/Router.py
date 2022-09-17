import sys
def input():
    return sys.stdin.readline()

N = int(input())
q = [0] * N
p = 0
while True:
    a = int(input())
    if a == -1:
        break
    elif a == 0:
        q.pop(0)
        q.append(0)
        p -= 1
    else:
        if q[-1]:
            continue
        else:
            q[p] = a
            p += 1
if sum(q):
    for i in q:
        if i:
            print(i, end=' ')
else:
    print('empty')