K = int(input())
for k in range(1, K+1):
    score = list(map(int, input().split()))
    score = score[1:]
    # print(score)
    score.sort()
    A, B, C = score[-1], score[0], 0
    for i in range(len(score)-1):
        if score[i+1]-score[i] > C:
            C = score[i+1]-score[i]
    print(f'Class {k}')
    print(f'Max {A}, Min {B}, Largest gap {C}')