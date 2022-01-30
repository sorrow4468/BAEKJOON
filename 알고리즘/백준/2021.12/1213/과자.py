a, b, c = map(int, input().split())

result = c - (a * b)

if result < 0:
    print(abs(result))
else:
    print(0)