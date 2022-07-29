N, M = map(int, input().split())
L = set() # listened
for n in range(N): L.add(input())
result = []
for m in range(M):
    s = input()
    if s in L:
        result.append(s)
result.sort()
print(len(result))
for r in result: print(r)