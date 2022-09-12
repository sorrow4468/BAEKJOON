N = int(input())
for n in range(N):
    if n%2 == 0:
        print('* ' * N)
    else:
        print(' *' * N)