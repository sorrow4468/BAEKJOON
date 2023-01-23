for _ in range(int(input())):
    N = input()
    print('YES' if N == str(int(N)**2)[-len(N):] else 'NO')