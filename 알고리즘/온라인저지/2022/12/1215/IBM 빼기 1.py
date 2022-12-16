N = int(input())
for tc in range(1, N+1):
    print('String #{}'.format(tc))
    for i in input():
        tmp = ord(i)+1
        print(chr(tmp) if tmp <= 90 else 'A', end='')
    if tc == N: break
    print('\n')