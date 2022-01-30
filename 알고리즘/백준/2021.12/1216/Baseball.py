T = int(input())

for tc in range(T):
    Y = K = 0
    
    for i in range(9):
        
        y, k = map(int, input().split())

        Y += y
        K += k

    if Y > K:
        print('Yonsei')
    elif K > Y:
        print('Korea')
    else:
        print('Draw')