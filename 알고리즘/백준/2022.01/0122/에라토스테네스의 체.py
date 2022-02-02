n, K = map(int, input().split())                    # 소수를 찾을 범위
a = [False,False] + [True]*(n-1)    # 0 ~ n 까지의 숫자 리스트

cnt = 0

for i in range(2,n+1):              # 2 ~ n까지 반복
    if a[i]:                          # 2부터 시작, 해당 숫자가 지워지지 않고 남아있는 소수라면 
        for j in range(i, n+1, i):    # 해당 소수의 배수들을 
            if a[j] == False:
                continue
            a[j] = False                # 리스트에서 전부 False로 만들기
            cnt += 1
            if cnt == K:
                print(j)
 
