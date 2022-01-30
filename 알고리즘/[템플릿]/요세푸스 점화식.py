def josephus(N, K):
    if N == 1:
        return 1
    else:
        return ((josephus(N-1, K) + K - 1) % N) + 1

N, K = map(int, input().split())
print(josephus(N, K))