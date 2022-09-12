N = int(input())

scores = list(map(int, input().split()))

maxx = 0
minn = 1000

for s in scores:
    if s >= maxx:
        maxx = s
    
    if s <= minn:
        minn = s

print(maxx-minn)