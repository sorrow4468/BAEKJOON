cards = list(range(21))

# a, b = 5, 10
# print(cards[a:b+1])
# print(cards[b:a-1:-1])

for i in range(10):
    a, b = map(int, input().split())

    cards[a:b+1] = cards[b:a-1:-1]

print(*cards[1:])