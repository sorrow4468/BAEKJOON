T = int(input())

for t in range(T):
    N = int(input())

    sumC = 0

    tmp = 0

    for n in range(N):
        C, G = map(float, input().split())
        C = int(C)

        sumC += C
        
        tmp += C * G

    print('{} {:.1f}'.format(sumC, tmp/sumC))

