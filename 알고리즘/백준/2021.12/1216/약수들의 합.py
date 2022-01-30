while True:
    n = int(input())

    if n == -1:
        break

    measure_counts = [0 for _ in range(n+1)]
    measures = []

    for i in range(1, n+1):
        if not measure_counts[i]:
            if n % i == 0:
                measure_counts[i] = 1
                measure_counts[n//i] = 1
                measures.append(i)
                measures.append(n//i)

    measures.sort()

    if sum(measures[:len(measures)-1]) == n:
        print('{} = '.format(n), end='')
        for i in range(len(measures)-1):
            print(measures[i], end='')
            if i != len(measures)-2:
                print(' + ', end='')
        print()    
    else:
        print('{} is NOT perfect.'.format(n))
    
