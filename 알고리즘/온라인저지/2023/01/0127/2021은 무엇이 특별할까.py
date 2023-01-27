def prime_list(size):
    sieve = [True]*(size+1)
    for i in range(2, int(size**0.5)+1):
        if sieve[i]:
            for j in range(i+i, size+1, i):
                sieve[j] = False
    return [i for i in range(2, size+1) if sieve[i]]

N = int(input())
primes = prime_list(5500)
for i in range(len(primes)-1):
    is_special = primes[i]*primes[i+1]
    if is_special > N:
        print(is_special)
        break