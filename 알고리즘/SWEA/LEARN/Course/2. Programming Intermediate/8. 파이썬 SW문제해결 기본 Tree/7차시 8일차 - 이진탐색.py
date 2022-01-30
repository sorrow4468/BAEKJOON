def makeTree(n):
    global count

    if n <= N:
        makeTree(n*2)

        tree[n] = count
        count += 1

        makeTree(n*2 + 1)

TC = int(input())
for tc in range(TC):
    N = int(input())
    
    tree = [0 for _ in range(N+1)]
    count = 1

    makeTree(1)

    print('#{} {} {}'.format(tc, tree[1], tree[N//2]))
 