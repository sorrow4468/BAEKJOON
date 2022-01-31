N = int(input())

i = 1

for n in range(N):
    a = ((N*2-1)-i)//2
    print(' ' * a, '*' * i, sep='')
    i += 2

i -= 2

for n in range(N-1):
    i -= 2
    a = ((N*2)-i)//2
    print(' ' * a, '*' * i, sep='')