scores = list(map(int, input().split()))
maxx = [100, 100, 200, 200, 300, 300, 400, 400, 500]
coffee, hacker = 0, 0
for i in range(9):
    S, M = scores[i], maxx[i]
    if S>M:
        hacker = 1
    coffee += S
if hacker:
    print('hacker')
else:
    if coffee<100:
        print('none')
    else:
        print('draw')