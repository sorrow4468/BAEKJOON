N = int(input())

result = 0

tmp = 1

while tmp <= N:
    if tmp == N:
        result = 1
        break

    tmp *= 2

print(result)