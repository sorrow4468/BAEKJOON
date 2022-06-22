N = int(input())
cow = ['Zero'] + [0]*10 # 0:미발견, 1:왼쪽, 2:오른쪽
result = 0
for n in range(N):
    c, lr = map(int, input().split())
    lr += 1
    if cow[c]:
        if cow[c] != lr: # 길을 건넜음
            result += 1
            cow[c] = lr
    else: # not cow[c]
        cow[c] = lr
print(result)