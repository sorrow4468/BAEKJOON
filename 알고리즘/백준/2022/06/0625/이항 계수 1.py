from math import factorial as fact

N, K = map(int, input().split())
result = fact(N) / (fact(K) * fact(N-K))
print(f'{result:.0f}')