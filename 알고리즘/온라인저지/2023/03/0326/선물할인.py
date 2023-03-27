N, B, A = map(int, input().split())
P = sorted(list(map(int, input().split())))
result = 0
summ = 0

for i in range(N):
    if summ+P[i]<=B:
        summ += P[i]
        result += 1
    else:
        if summ+(P[i]//2)<=B and A:
            summ += P[i]//2
            result += 1
            A -= 1
        else:
            break

print(summ, result)