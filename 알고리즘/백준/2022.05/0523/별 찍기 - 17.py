N = int(input())
start = N-1
last = N*2-1
middle = 1
for n in range(N):
    if n == 0:
        print(' '*start, '*', sep='')
        start -= 1
    elif n == N-1:
        print('*'*last)
    else:
        print(' '*start, end='')
        print('*', ' '*middle, '*', sep='')
        middle += 2
        start -= 1
