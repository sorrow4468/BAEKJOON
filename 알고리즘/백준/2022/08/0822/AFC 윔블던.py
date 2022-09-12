N, M = map(int, input().split())
if (N+M)%2 or N<M:
    print(-1)
else:
    print((N+M)//2, (N-M)//2)