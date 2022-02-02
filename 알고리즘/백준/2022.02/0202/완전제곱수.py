M = 0
N = 0

for i in range(2):
    if i == 0:
        M = int(input())
    elif i == 1:
        N = int(input())

i = 0
minn = 0
summ = 0

while True:
    i += 1
    pow = i ** 2
    if pow > N:
        break

    if pow >= M and pow <= N:
        if not minn:
            minn = pow
        
        summ += pow

if minn:
    print(summ, minn)
else:
    print(-1)