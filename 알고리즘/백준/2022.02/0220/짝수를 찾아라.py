T = int(input())

for t in range(T):
    nums = list(map(int, input().split()))

    minn = 100
    summ = 0

    for n in nums:
        if not n%2:
            summ += n

            if n < minn:
                minn = n
    
    print(summ, minn)