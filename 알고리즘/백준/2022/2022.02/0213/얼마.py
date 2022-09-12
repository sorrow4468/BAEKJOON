T = int(input())

for t in range(T):
    S = int(input())
    N = int(input())
    
    result = S

    for n in range(N):
        q, p = map(int, input().split())

        result += q * p
    
    print(result)