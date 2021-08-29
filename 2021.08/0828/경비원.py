import sys

W, H = map(int, sys.stdin.readline().split())
market_count = int(sys.stdin.readline())
markets = []
for _ in range(market_count):
    markets.append(list(map(int, sys.stdin.readline().split())))
dgnswe, dgdist = map(int, sys.stdin.readline().split())

result = 0

for i in range(market_count):
    if (markets[i][0] == 1 and dgnswe == 2) or (markets[i][0] == 2 and dgnswe == 1):
        result += H
        tmp1 = markets[i][1] + dgdist
        tmp2 = W - markets[i][1] + W - dgdist
        if tmp1 < tmp2:
            result += tmp1
        else:
            result += tmp2

    elif (markets[i][0] == 3 and dgnswe == 4) or (markets[i][0] == 4 and dgnswe == 3):
        result += W
        tmp1 = markets[i][1] + dgdist
        tmp2 = H - markets[i][1] + H - dgdist
        if tmp1 < tmp2:
            result += tmp1
        else:
            result += tmp2

    elif markets[i][0] == dgnswe:
        result += abs(markets[i][1] - dgdist)
    else: # 좌 우 일때
        if markets[i][0] == 1:
            if dgnswe == 3:
                result += markets[i][1] + dgdist
            else:
                result += W - markets[i][1] + dgdist
        if markets[i][0] == 2:
            if dgnswe == 3:
                result += markets[i][1] + H - dgdist
            else:
                result += W - markets[i][1] + H - dgdist
        if markets[i][0] == 3:
            if dgnswe == 1:
                result += markets[i][1] + dgdist
            else:
                result += H - markets[i][1] + dgdist
        if markets[i][0] == 4:
            if dgnswe == 1:
                result += markets[i][1] + W - dgdist
            else:
                result += H - markets[i][1] + W - dgdist

print(result)

