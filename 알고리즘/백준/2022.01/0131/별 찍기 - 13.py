N = int(input())

i = 1

for n in range(N):
    print('*' * i)
    i += 1

i -= 1

for n in range(N-1):
    i -= 1
    print('*' * i)
