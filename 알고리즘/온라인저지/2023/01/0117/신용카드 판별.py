for _ in range(int(input())):
    card = list(map(int, list(input())))
    result = 0
    for i in range(0, 16, 2):
        card[i] = card[i]*2
        if card[i] > 9:
            card[i] = (card[i]%10) + 1
        result += card[i] + card[i+1]
    print('F' if result%10 else 'T')