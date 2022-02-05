N = int(input())

result = 0

for n in range(N):
    s, a = map(int, input().split())

    result += a%s

print(result)