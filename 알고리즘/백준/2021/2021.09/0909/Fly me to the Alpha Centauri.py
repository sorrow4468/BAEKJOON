import sys
def input():
    return sys.stdin.readline()

def how_many_times(x):
    a = 1
    i = 1
    if a == x:
        return i
    b = 1
    a = a+b
    i += 1
    if a == x:
        return i
    while True:
        b += 1
        a = a+b
        i += 1
        if a >= x:
            break
        a = a+b
        i += 1
        if a >= x:
            break
    return i

T = int(input())
for t in range(T):
    x, y = map(int, input().split())
    d = y-x
    print(how_many_times(d))