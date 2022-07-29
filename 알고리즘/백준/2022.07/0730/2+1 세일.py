N = int(input())
P = [] # price
for n in range(N): P.append(int(input()))
P.sort(reverse=True)
result = 0
for i in range(0, N, 3):
    try:
        result += sum(P[i:i+2])
    except:
        result += P[i:]
print(result)