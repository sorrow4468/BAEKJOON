a = list(map(int, input().split()))

dice_num_count = [0 for _ in range(6)]

for i in a:
    dice_num_count[i-1] += 1

same_or_max = 0
result = 0

if 3 in dice_num_count:
    same_or_max = dice_num_count.index(3) + 1
    result = 10000 + same_or_max * 1000
elif 2 in dice_num_count:
    same_or_max = dice_num_count.index(2) + 1
    result = 1000 + same_or_max * 100
else:
    same_or_max = max(a)
    result = same_or_max * 100

print(result)
