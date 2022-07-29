import sys

def input():
    return sys.stdin.readline().rstrip()

N, M = map(int, input().split())
P = ['' for _ in range(N+1)] # pokemon
for n in range(1, N+1):
    P[n] = input()
for m in range(M):
    Q = input()
    try: # int
        print(P[int(Q)])
    except: # str
        print(P.index(Q))