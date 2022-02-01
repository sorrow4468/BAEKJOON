now = 0
result = 0

for t in range(4):
    off, on = map(int, input().split())

    now += (on-off)

    if now > result:
        result = now

print(result)