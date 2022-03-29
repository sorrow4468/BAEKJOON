T = int(input())
for t in range(T):
    N = int(input())
    jbox = [['J']*N for _ in range(N)]
    jbox[0] = jbox[-1] = ['#']*N
    for i in range(1, N-1):
        jbox[i][0] = jbox[i][-1] = '#'
    for i in range(N):
        for j in range(N):
            print(jbox[i][j], end='')
        print()
    print()