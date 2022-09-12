N = int(input())

i = N*2-1

for n in range(N):
    a = (((N*2)-1)-i)//2
    print(' ' * a, '*' * i, sep='')
    i -= 2

i = 3

for n in range(N-1):
    a = (((N*2)-1)-i)//2
    print(' ' * a, '*' * i, sep='')
    i += 2