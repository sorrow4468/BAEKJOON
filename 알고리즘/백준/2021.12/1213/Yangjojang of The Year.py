T = int(input())

for tc in range(T):
    N = int(input())

    YOTY = ''
    YOTY_drink = 0

    for n in range(N):
        univ = input().split()
        if int(univ[1]) > YOTY_drink:
            YOTY_drink = int(univ[1])
            YOTY = univ[0]
    
    print(YOTY)
