N = int(input())
crew = list(map(int, input().split()))
result = 0
for i in range(1, N+1):
    if crew[i-1] != i:
        result += 1
print(result)