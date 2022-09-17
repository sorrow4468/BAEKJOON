data = list(map(int, input().split()))
result = 0
for dt in data:
    result += dt**2
print(result%10)