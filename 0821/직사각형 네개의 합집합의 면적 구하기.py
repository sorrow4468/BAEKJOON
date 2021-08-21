"""
좌표평면배열을 만들어서
직사각형들을 1로 저장하고
저장하는 과정에서 겹치면 continue
저장된 1들을 전부 출력"""

arr = [[0]*101 for _ in range(101)] # 0번째칸 추가해서 인덱스와 숫자 일치
for tc in range(4): # 모든 케이스는 4개의 직사각형
    x1, y1, x2, y2 = map(int, input().split()) # 좌표들
    for i in range(y1, y2): # y좌표 for문 먼저
        for j in range(x1, x2): # x좌표
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