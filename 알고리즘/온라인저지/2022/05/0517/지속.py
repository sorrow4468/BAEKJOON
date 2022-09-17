N = input()
result = 0
while len(N) > 1:
    tmp = 1
    for n in N:
        tmp *= int(n)
    N = str(tmp)
    result += 1
print(result)