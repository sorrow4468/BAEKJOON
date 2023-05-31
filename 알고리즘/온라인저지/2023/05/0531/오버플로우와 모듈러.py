N, M = map(int, input().split())
result = 1
for i in list(map(int, input().split())):
    result *= i%M
    result %= M
print(result)