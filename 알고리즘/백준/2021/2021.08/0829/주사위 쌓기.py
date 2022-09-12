import sys

dice_count = int(sys.stdin.readline())
dices = []
for d in range(dice_count):
    dices.append(list(map(int, sys.stdin.readline().split())))
result = 0
for j in range(6):
    max_sum = 0
    up = 0
    for i in range(dice_count):
        dice_opposite = {
            dices[i][0]:dices[i][5], 
            dices[i][1]:dices[i][3],
            dices[i][2]:dices[i][4],
            dices[i][3]:dices[i][1],
            dices[i][4]:dices[i][2],
            dices[i][5]:dices[i][0]
            }
        tmp = [*dices[i]]
        try:
            if up == 0:
                tmp.remove(dices[i][j])
                tmp.remove(dice_opposite[dices[i][j]])
                up = dice_opposite[dices[i][j]]
                max_sum += max(tmp)
            else:
                tmp.remove(up)
                tmp.remove(dice_opposite[up])
                up = dice_opposite[up]
                max_sum += max(tmp)
        except:
            pass
    if result < max_sum:
        result = max_sum
print(result)