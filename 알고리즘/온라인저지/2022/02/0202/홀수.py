summ = 0
minn = 100
is_odd = False

for _ in range(7):
    num = int(input())

    if num%2:
        if num < minn:
            minn = num
        summ += num
        if not is_odd:
            is_odd = True

if is_odd:
    print(summ)
    print(minn)
else:
    print(-1)