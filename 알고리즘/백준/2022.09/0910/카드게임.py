A_card = list(map(int, input().split()))
B_card = list(map(int, input().split()))
A_win = B_win = draw = 0
for i in range(10):
    if A_card[i] > B_card[i]: A_win += 1
    elif A_card[i] < B_card[i]: B_win += 1
    else: draw += 1
result = ''
if A_win > B_win: result = 'A'
elif A_win < B_win: result = 'B'
else: result = 'D'
print(result)