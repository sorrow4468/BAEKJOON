n = int(1e4)
a = [False,False] + [True]*(n-1)
primes = []
for i in range(2, n+1):
    if a[i]:
        primes.append(i)
    for j in range(2*i, n+1, i):
        a[j] = False
for t in range(int(input())):
    N = int(input())
    result = []
    for prime in primes:
        if prime > N: break
        if N-prime in primes:
            tmp = sorted((N-prime, prime))
            if tmp not in result:
                result.append(tmp)
    print(*result[-1])