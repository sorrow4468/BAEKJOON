import sys

input = sys.stdin.readline

result = 0
for _ in range(int(input().rstrip())):
    dices = list(map(int, input().rstrip().split()))
    count_arr = [0]*11
    for dice in dices: count_arr[dice] += 1
    tmp = 0
    if 4 in count_arr:
        tmp += 50000 + count_arr.index(4)*5000
    elif 3 in count_arr:
        tmp += 10000 + count_arr.index(3)*1000
    elif count_arr.count(2) == 2:
        tmp += 2000
        for i in range(11):
            if count_arr[i] == 2: 
                tmp += i*500
    elif 2 in count_arr:
        tmp += 1000 + count_arr.index(2)*100
    else: 
        tmp += max(dices)*100
    result = max(result, tmp)
print(result)