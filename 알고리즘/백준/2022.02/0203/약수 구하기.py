N, K = map(int, input().split())

measures = []

for i in range(1, int(N**0.5)+1):
    if not N%i:
        measures.append(i)
        
tmp = measures[::-1]

for t in tmp:
    if N//t != N**0.5:
        measures.append(N//t)

if len(measures) >= K:
    print(measures[K-1])
else:
    print(0)