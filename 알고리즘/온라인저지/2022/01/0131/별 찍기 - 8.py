N = int(input())

i = 0

for n in range(N):
    i += 1
    a = (N-i) * 2
    print('*' * i, ' ' * a, '*' * i, sep='')

for n in range(N-1):
    i -= 1
    a = (N-i) * 2
    print('*' * i, ' ' * a, '*' * i, sep='')
