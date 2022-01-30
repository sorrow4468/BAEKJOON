x = [1, 3, 11, 15, 23, 28, 37, 52, 85, 100]

print('[', end='')

for i in x:
    if i % 2 == 0:
        print(i, end='')
        if i != x[-1]:
            print(end=', ')

print(']')