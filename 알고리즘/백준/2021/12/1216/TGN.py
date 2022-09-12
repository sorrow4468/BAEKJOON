N = int(input())

for n in range(N):
    r, e, c = map(int, input().split())

    fee = e-c

    if fee > r:
        print('advertise')
    elif fee < r:
        print('do not advertise')
    else:
        print('does not matter')