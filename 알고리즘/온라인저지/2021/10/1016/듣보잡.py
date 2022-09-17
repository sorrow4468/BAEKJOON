N, M = map(int, input().split())

a = set()

for n in range(N):
    a.add(input())

result = []

for m in range(M):
    b = input()
    if b in a:
        result.append(b)

print(len(result))
result.sort()
for r in result:
    print(r)