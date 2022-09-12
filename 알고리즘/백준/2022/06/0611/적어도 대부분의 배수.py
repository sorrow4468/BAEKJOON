nums = list(map(int, input().split()))
maxx = 10000000000
for i in range(1, maxx):
    a = 0
    for n in nums:
        if not i%n:
            a += 1
    if a >= 3:
        print(i)
        exit()