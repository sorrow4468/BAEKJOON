card = dict()
for n in range(int(input())):
    tmp = int(input())
    try:
        card[tmp] += 1
    except:
        card[tmp] = 1
num = sorted(list(card))
maxx = 0
result = 0
for n in num:
    if card[n] > maxx:
        maxx = card[n]
        result = n
print(result)