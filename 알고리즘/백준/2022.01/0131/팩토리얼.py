N = int(input())

result = 1

if N > 1:
    for i in range(2, N+1):
        result *= i
    print(result)
else:
    print(1)
