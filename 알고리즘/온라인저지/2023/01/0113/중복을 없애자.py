while True:
    tmp = input()
    if tmp == '0': break
    tmp = list(map(int, tmp.split()))
    N, arr = tmp[0], tmp[1:]
    last = arr[0]
    print(last, end=' ')
    for a in arr[1:]:
        if a != last:
            last = a
            print(last, end=' ')
    print('$')