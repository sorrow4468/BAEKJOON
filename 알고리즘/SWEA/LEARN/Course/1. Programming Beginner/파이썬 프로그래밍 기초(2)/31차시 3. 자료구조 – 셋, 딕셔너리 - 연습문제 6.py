N = int(input())

result = {}

for i in range(1, N+1):
    result.update({i:i*i})

print(result)