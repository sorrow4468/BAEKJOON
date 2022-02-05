N = int(input())

result = 0

for n in range(N):
    if result:
        result -= 1
    result += int(input())

print(result)
    