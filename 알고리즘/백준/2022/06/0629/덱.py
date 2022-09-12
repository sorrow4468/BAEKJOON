from collections import deque
import sys
def input():
    return sys.stdin.readline()

D = deque()
for i in range(int(input())):
    tmp = input().split()
    if tmp[0] == 'push_front':
        D.appendleft(tmp[1])
    elif tmp[0] == 'push_back':
        D.append(tmp[1])
    elif tmp[0] == 'pop_front':
        print(D.popleft()) if D else print(-1)
    elif tmp[0] == 'pop_back':
        print(D.pop()) if D else print(-1)
    elif tmp[0] == 'size':
        print(len(D))
    elif tmp[0] == 'empty':
        print(0) if D else print(1)
    elif tmp[0] == 'front':
        print(D[0]) if D else print(-1)
    elif tmp[0] == 'back':
        print(D[-1]) if D else print(-1)