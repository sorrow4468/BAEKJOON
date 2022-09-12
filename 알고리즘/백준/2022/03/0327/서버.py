N, T = map(int, input().split())
works = list(map(int, input().split()))
result = 0
for work in works:
    T -= work
    if T < 0:
        break
    result += 1
print(result)