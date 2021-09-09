import sys
def input():
    return sys.stdin.readline()



N = int(input())
q = [0] * N
pnt = 0
cnt = 0
back = 0
for n in range(N):
    order = input().split()
    if order[0] == 'push':
        q[back] = order[1]
        cnt += 1
        back += 1
    elif order[0] == 'pop':
        if cnt:
            print(q[pnt])
            pnt += 1
            cnt -= 1
        else:
            print(-1)
    elif order[0] == 'size':
        print(cnt)
    elif order[0] == 'empty':
        if cnt:
            print(0)
        else:
            print(1)
    elif order[0] == 'front':
        if cnt:
            print(q[pnt])
        else:
            print(-1)
    elif order[0] == 'back':
        if cnt:
            print(q[back-1])
        else:
            print(-1)