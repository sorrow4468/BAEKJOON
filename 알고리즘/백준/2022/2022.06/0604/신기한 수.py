# print(list(str(392)))
N = int(input())
i = 1
result = 0
for n in range(1, N+1):
    tmp = 0
    for j in list(str(n)):
        tmp += int(j)
    if not n%tmp:
        result += 1
print(result)