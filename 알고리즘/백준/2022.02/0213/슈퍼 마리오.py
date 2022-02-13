now = int(input())
ans_found = False
result = 0

for _ in range(9):
    num = int(input())
    tmp = now + num

    if ans_found:
        continue

    if tmp >= 100 and num < 100:
        if abs(tmp-100) <= abs(100-now):
            result = tmp
        else:
            result = now
        ans_found = True

    now += num

if now <= 100:
    result = now

print(result)