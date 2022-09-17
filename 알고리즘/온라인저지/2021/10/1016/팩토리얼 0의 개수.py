N = int(input())

result = 1

for i in range(1, N+1):
    result *= i

print(len(str(result)) - len(str(result).rstrip('0')))