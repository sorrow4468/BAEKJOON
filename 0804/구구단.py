N = int(input()) # 1 < N <= 9 인 N을 입력받아서
for i in range(1, 10): # 1부터 9까지 순회하면서 
    print(f'{N} * {i} = {N*i}') # 구구단을 출력