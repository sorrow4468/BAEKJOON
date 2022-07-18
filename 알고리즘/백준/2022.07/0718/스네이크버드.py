N, L = map(int, input().split())
F = list(map(int, input().split())) # fruits
F.sort()
# print(F)
for i in range(len(F)):
    if L >= F[i]:
        L += 1
print(L)