while True:
    N = int(input())
    if N:
        if str(N) == str(N)[::-1]:
            print('yes')
        else:
            print('no')
    else:
        break