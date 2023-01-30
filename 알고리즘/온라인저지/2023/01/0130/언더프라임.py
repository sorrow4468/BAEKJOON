def prime_list(size):
    sieve = [True]*(size+1)
    for i in range(2, int(size**0.5)+1):
        if sieve[i]:
            for j in range(i+i, size+1, i):
                sieve[j] = False
    return [i for i in range(2, size+1) if sieve[i]]
    
def factorization(x):
    i = 0
    d = primes[i]
    answer = 0
    while d <= x:
        if x % d == 0:
            answer += 1
            x = x // d
        else:
            i += 1
            d = primes[i]
    return answer


primes = prime_list(int(1e6))
A, B = map(int, input().split())
result = 0
for i in range(A, B+1):
    if factorization(i) in primes:
        result += 1
print(result)