cospas = []
for snack in ['S', 'N', 'U']:
    cost, weight = map(int, input().split())
    cost *= 10
    if cost>=5000: cost -= 500
    cospas.append((snack, weight/cost))
cospas.sort(key=lambda x:-x[1])
print(cospas[0][0])