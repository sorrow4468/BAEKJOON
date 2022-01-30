T = int(input())

for t in range(1, T+1):
    N = int(input())

    counts = [0] * (10)

    num = input()
    
    for n in num:
        counts[int(n)] += 1
    
    cnt = 0
    result = 0

    if counts.count(max(counts)) == 1:
        result = counts.index(max(counts))
        cnt = max(counts)
    else: # != 1
        for i in range(9, -1, -1):
            if counts[i] == max(counts):
                result = i
                cnt = counts[i]
                break

    print('#{} {} {}'.format(t, result, cnt))