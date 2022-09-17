T = int(input())
for t in range(T):
    N = int(input())
    result = 1000000001
    mbti = input().split()
    if N > 48:
        result = 0
    else:
        for i in range(N-2):
            for j in range(i+1, N-1):
                for k in range(j+1, N):
                    A = mbti[i]
                    B = mbti[j]
                    C = mbti[k]
                    D = 0 # distance
                    # print(A, B, C)
                    for l in range(4):
                        if A[l] != B[l]:
                            D += 1
                        if B[l] != C[l]:
                            D += 1
                        if C[l] != A[l]:
                            D += 1
                    if D < result:
                        result = D
    print(result)