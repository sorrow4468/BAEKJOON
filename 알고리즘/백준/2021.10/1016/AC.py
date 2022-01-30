from collections import deque
import sys

T = int(sys.stdin.readline())

for t in range(T):
    order = sys.stdin.readline().rstrip()
    order.replace('RR', '')
    N = int(sys.stdin.readline())
    arr = sys.stdin.readline().rstrip()[1:-1].split(',')
    q = deque(arr)

    rev, left, right = False, 0, len(q)-1
    flag = False

    if N == 0:
        q = []
        right = 0

    for o in order:
        if o == 'R':
            if rev:
                rev = False
            else:
                rev = True
        elif o == 'D':
            if len(q) < 1:
                flag = True
                print('error')
                break
            else:
                if rev:
                    q.pop()
                else:
                    q.popleft()
    
    if not flag:
        if rev:
            q.reverse()
            print('['+','.join(q)+']')
        else:
            print('['+','.join(q)+']')