A_atk, A_hp = map(int, input().split())
B_atk, B_hp = map(int, input().split())
while A_hp > 0 and B_hp > 0:
    A_hp -= B_atk
    B_hp -= A_atk
if A_hp > 0:
    result = 'PLAYER A'
elif B_hp > 0:
    result = 'PLAYER B'
else:
    result = 'DRAW'
print(result)