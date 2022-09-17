for _ in range(int(input())):
    N = int(input())
    result = []
    for n in range(1, (N//2)+1):
        A, B = n, N-n
        if A != B:
            result.append((A, B))
    print(f'Pairs for {N}: ', end='')
    cnt = 0
    for r in result:
        print(*r, end='')
        cnt += 1
        if cnt != len(result):
            print(', ', end='')
    print()
