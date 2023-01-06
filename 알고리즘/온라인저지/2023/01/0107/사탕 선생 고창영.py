T = int(input())
for t in range(T):
    input()
    N = int(input())
    arr = [int(input()) for _ in range(N)]
    print('NO' if sum(arr)%N else 'YES')