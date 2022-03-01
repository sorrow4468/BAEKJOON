players = list(map(int, input().split()))

players.sort()

tmp = [players[0] + players[3], players[1] + players[2]]

tmp.sort()

print(tmp[1] - tmp[0])