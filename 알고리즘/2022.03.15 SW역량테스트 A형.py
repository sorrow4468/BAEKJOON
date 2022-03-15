"""
어딜 갈 수 있는가
잡기 전
1 2 3
1을 잡은 후
2 3 -1
3을 잡은 후
2 -1 -3

dfs돌 필요도 없다 좌표찾고 더하기빼기로도 가능

가지고 있는 최소값보다 커지면 가지치기
"""
import tabnanny


def dfs(c, y, x, h, can_go):
    global monster_visited, customer_visited, minn
    # print(c)
    for mnc in monsters_and_customers:
        if mnc[0] == c:
            h += abs(y-mnc[1]) + abs(x-mnc[2])
            if h > minn:
                continue
            y = mnc[1]
            x = mnc[2]
            if c > 0:
                can_go.append((can_go.pop(can_go.index(c)) * (-1)))
            elif c < 0:
                can_go.pop(can_go.index(c))
            if not can_go:
                if h < minn:
                    minn = h
                    # print('renew minn!!', minn)

            # print(can_go)
            for g in can_go:
                if g > 0:
                    if not monster_visited[g-1]:
                        dfs(g, y, x, h, can_go)
                elif g < 0:
                    if not customer_visited[g*(-1)-1]:
                        dfs(g, y, x, h, can_go)


T = int(input())
for t in range(1, T+1):
    N = int(input())
    arr = []
    how_many_customer = 0
    for n in range(N):
        tmp = list(map(int, input().split()))
        if max(tmp) > how_many_customer:
            how_many_customer = max(tmp)
        arr.append(tmp)
    # print(how_many_customer)
    monsters_and_customers = []
    for i in range(N):
        for j in range(N):
            if arr[i][j] != 0:
                monsters_and_customers.append([arr[i][j], i, j])
    # print(monsters_and_customers)
    monsters = list(range(1, how_many_customer+1))
    # print(monsters)
    minn = 10**6
    for m in monsters:
        monster_visited = [0] * how_many_customer
        customer_visited = [0] * how_many_customer
        h = 0
        x = y = 0    
        dfs(m, y, x, h, list(range(1, how_many_customer+1)))
    print('#{} {}'.format(t, minn))