while True:
    try:
        S, T = input().split()
        j = 0
        tmp = ''
        result = 'No'
        for i in range(len(T)):
            if T[i] == S[j]:
                tmp += T[i]
                j += 1
            if j >= len(S):
                break
        # print(tmp)
        if tmp == S:
            result = 'Yes'
        print(result)
    except:
        exit()