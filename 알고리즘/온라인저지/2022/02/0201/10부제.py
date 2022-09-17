D = int(input())
cars = list(map(int, input().split()))

result = 0

for c in cars:
    if c == D:
        result += 1

print(result)