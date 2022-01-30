x = list(map(int, input().split(', ')))

for i in x:
    if i%2:
        if i == x[-1]:
            print(i)
        else:
            print(i, end=', ')