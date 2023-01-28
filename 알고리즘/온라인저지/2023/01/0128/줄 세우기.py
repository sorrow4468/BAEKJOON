players = [input() for _ in range(int(input()))]
if players == sorted(players):
    print('INCREASING')
elif players == sorted(players, reverse=True):
    print('DECREASING')
else: print('NEITHER')