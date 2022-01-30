x = input().split(', ')

x.sort()

for i in x:
    if i == x[-1]:
        print(i)
    else:
        print(i, end=', ')