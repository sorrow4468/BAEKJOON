N = int(input())

i = 1

for n in range(N):
    a = (((N*2)-1)-i)//2
    print(' ' * a, '*' * i, sep='')
    i += 2