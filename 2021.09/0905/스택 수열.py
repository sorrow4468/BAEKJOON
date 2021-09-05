import sys
from types import SimpleNamespace

n = int(sys.stdin.readline())
ori = list(range(2, n+1))
tmp = [1]
ope = ['+']

for _ in range(n):
    if not tmp:
        tmp.append(ori.pop(0))
        ope.append('+')
    num = int(sys.stdin.readline())
    if num == tmp[-1]:
        tmp.pop()
        ope.append('-')    
    elif num < tmp[-1]:
        print('NO')
        exit()
    else:
        while num != tmp[-1]:
            tmp.append(ori.pop(0))
            ope.append('+')
        tmp.pop()
        ope.append('-')    
    

for o in ope:
    print(o)