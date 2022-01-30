A = list(range(1, 12+1))

T = int(input())

for t in range(1, T+1):
    N, K = map(int, input().split())

    n = len(A)
    cnt = 0

    for i in range(1<<n):
        tmp = set()
        for j in range(n):
            if i&(1<<j):
                tmp.add(A[j])
        if sum(tmp) == K and len(tmp) == N:
            cnt += 1
            
    print('#{} {}'.format(t, cnt))