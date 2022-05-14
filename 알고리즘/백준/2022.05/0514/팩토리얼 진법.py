table = []
a = 1
for i in range(1, 6):
    table.append(a*i)
    a *= i
while True:
    N = input()
    if N == '0':
        break
    M = len(N)
    N = N[::-1]
    result = 0
    for i in range(M):
        result += int(N[i])*table[i]
    print(result)
