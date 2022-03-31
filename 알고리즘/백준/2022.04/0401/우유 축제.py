N = int(input())
milk = list(map(int, input().split()))
now = 0
result = 0
for m in milk:
    if now == m:
        result += 1
        now += 1
        now %= 3
print(result)