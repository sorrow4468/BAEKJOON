N = int(input())
player = []
for n in range(N):
    player.append(list(map(int, input().split())))
result = [0] * N
for i in range(N): # 플레이어
    for j in range(3): # 점수들
        switch = True
        for k in range(N):
            if player[i][j] == player[k][j] and i != k:
                switch = False
        if switch:
            result[i] += player[i][j]
for r in result:
    print(r)