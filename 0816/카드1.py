N = int(input())
deck = list(range(1, N+1))
new_deck = []
for n in range(N):
    if len(deck) == 1:
        new_deck += deck
    else:
        new_deck.append(deck.pop(0))
        deck.append(deck.pop(0))
print(*new_deck)