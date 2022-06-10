from math import factorial as fact

for t in range(int(input())):
    N, M = map(int, input().split())
    print(fact(M)//(fact(N)*fact(M-N)))