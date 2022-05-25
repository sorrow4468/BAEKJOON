N = int(input())
start = N-1
middle = 1
for n in range(N):
    print(' '*start, end='')
    if n == 0:
        print('*')
        start -= 1
    else:
        print('*', ' '*middle, '*', sep='')
        middle += 2
        start -= 1
