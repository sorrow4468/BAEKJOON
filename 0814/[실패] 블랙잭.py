N, M = map(int, input().split())
cards = list(map(int, input().split()))
blackjack = []
for i in range(N-2):
    for j in range(i+1, N-1):
        for k in range(j+1, N):
            is_this_blackjack = cards[i]+cards[j]+cards[k]
            if is_this_blackjack not in blackjack:
                blackjack.append(is_this_blackjack)
if M in blackjack:
    print(M)
else:
    blackjack.append(M)
    blackjack.sort()
    if abs(blackjack[blackjack.index(M) - 1] - M) < abs(blackjack[blackjack.index(M) + 1] - M):
        print(blackjack[blackjack.index(M) - 1])
    else:
        print(blackjack[blackjack.index(M) + 1])
