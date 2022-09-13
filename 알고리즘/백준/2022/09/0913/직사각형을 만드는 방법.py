N = int(input())
result = 0
for i in range(1, int(N**0.5)+1):
    tmp = N//i - (i-1)
    result += tmp
print(result)