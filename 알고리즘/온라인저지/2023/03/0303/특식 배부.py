N = int(input())
result = 0
for i in list(map(int, input().split())):
    result += min((N, i))
print(result)