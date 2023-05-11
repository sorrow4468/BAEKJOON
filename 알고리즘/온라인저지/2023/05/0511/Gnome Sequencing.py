print('Gnomes:')
for i in range(int(input())):
    tmp = list(map(int, input().split()))
    A, B = sorted(tmp), sorted(tmp, reverse=True)
    result = 'Unordered'
    if (tmp == A or tmp == B):
        result = 'Ordered'
    print(result)