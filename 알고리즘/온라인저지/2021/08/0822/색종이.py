T = int(input())
arr = [[0]*101 for _ in range(101)]
for tc in range(T):
    x1, y1 = map(int, input().split())
    for i in range(y1, y1+10): # 색종이 크기는 10
        for j in range(x1, x1+10): 
            if arr[i][j]: # 값이 들어있으면
                continue # 컨티뉴
            else: # 아직 저장된 값이 없으면
                arr[i][j] = 1 # 1을 저장
                # 합집합은 or연산
                # True or로 넘어가기 때문에 값이 있으면 저장이 되지 않고
                # 합해지는 부분을 연산할 필요가 없어짐
area = 0 # 면적
for ar in arr: # 저장된 배열을 돌면서
    area += sum(ar) # 각 줄을 더해서 면적에 저장
print(area) # 출력