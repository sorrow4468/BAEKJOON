player_1_win = ['P R', 'R S', 'S P']
player_2_win = ['R P', 'S R', 'P S']
for t in range(int(input())):
    RSP = 0
    result = ''
    for n in range(int(input())):
        tmp = input()
        if tmp in player_1_win: RSP += 1
        elif tmp in player_2_win: RSP -= 1
    if RSP > 0: result = 'Player 1'
    elif RSP < 0: result = 'Player 2'
    else: result = 'TIE'
    print(result)