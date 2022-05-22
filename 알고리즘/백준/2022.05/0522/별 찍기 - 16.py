N = int(input())
start = N-1
for n in range(1, N+1):
    print(' ' * start, end='')
    for i in range(n):
        if i != n-1:
            print('*', end=' ')
        else:
            print('*')
    start -= 1