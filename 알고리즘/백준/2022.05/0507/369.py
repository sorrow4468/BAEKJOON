N = int(input())
result = 0
for n in range(1, N+1):
    for i in str(n):
        if i in '369':
            result += 1
print(result)