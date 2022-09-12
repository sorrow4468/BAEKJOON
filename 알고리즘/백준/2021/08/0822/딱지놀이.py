N = int(input())
for tc in range(N):
    A_cards = list(map(int, input().split()))
    A_count = A_cards.pop(0)
    B_cards = list(map(int, input().split()))
    B_count = B_cards.pop(0)
    A_cards.sort()
    B_cards.sort()
    A = [0] * 5 
    B = [0] * 5
    for a in A_cards:
        A[a] += 1
    for b in B_cards:
        B[b] += 1
    winner = ''
    for i in range(4, -1, -1):
        if i == 0:
            winner = 'D'
        if A[i] > B[i]:
            winner = 'A'
            break
        elif A[i] == B[i]:
            continue
        elif A[i] < B[i]:
            winner = 'B'
            break
    print(winner)
