N, M = map(int, input().split())
cards = list(map(int, input().split()))
blackjack = cards[0]+cards[1]+cards[2]
cards.sort()
for i in range(N-2):
    if cards[i] > M:
        break
    for j in range(i+1, N-1):
        if cards[i] + cards[j] > M:
            break
        for k in range(j+1, N):
            if cards[i] + cards[j] + cards[k] > M:
                break
            is_this_blackjack = cards[i]+cards[j]+cards[k]
            if is_this_blackjack == M:
                print(M)
                exit()
            else:
                if abs(M - is_this_blackjack) < abs(M - blackjack):
                    blackjack = is_this_blackjack
print(blackjack)