while True:
    a, b, c, d = map(int, input().split())
    if a == b == c == d == 0: break
    result = list(map(abs, [a-c, a-d, b-c, b-d]))
    print(min(result), max(result))