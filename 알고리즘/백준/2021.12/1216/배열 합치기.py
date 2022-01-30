N, M = map(int, input().split())

result = list(map(int, input().split())) + list(map(int, input().split()))

result.sort()

for r in result:
    print(r, end=' ')