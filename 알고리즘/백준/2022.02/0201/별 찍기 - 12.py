N = int(input())

i = 0

for n in range(N):
    i += 1
    print(' ' * (N-i), '*' * i, sep='')

for n in range(N-1):
    i -= 1
    print(' ' * (N-i), '*' * i, sep='')