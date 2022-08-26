while True:
    try:
        N, S = map(int, input().split())
        N += 1
        print(S//N)
    except: exit()