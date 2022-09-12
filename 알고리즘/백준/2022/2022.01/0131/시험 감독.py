N = int(input())

result = 0

A = list(map(int, input().split()))

B, C = map(int, input().split())

for a in A:
    a -= B
    result += 1

    if a > 0:
        result += a//C
        tmp = C * (a//C)
        if a != tmp:
            result += 1

print(result)