N = M = int(input())

for i in range(N):
    print((' ' * (N-M)), ('*' * M), sep='')
    M -= 1