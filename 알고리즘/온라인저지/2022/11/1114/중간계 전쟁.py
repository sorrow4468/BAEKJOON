import sys

input = sys.stdin.readline

gandalf = [1, 2, 3, 3, 4, 10]
sauron = [1, 2, 2, 2, 3, 5, 10]
for tc in range(1, int(input().rstrip())+1):
    G = S = 0
    gandalf_army = list(map(int, input().rstrip().split()))
    for i in range(6):
        G += gandalf[i]*gandalf_army[i]
    sauron_army = list(map(int, input().rstrip().split()))
    for i in range(7):
        S += sauron[i]*sauron_army[i]
    result = [
        'No victor on this battle field', # draw
        'Good triumphs over Evil', # gandalf win
        'Evil eradicates all trace of Good', # sauron win
    ]
    i = 0
    if G > S: i = 1
    elif G < S: i = 2
    print('Battle {}: {}'.format(tc, result[i]))