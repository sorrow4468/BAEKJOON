N = int(input())

arr = []

for n in range(N):
    arr.append(tuple(map(int, input().split()))) # 속도 향상을 위한 tuple()

arr.sort() # arr[x][0]을 기준으로 정렬
arr.sort(key=lambda x: x[1]) # 다시 한번 x[1]을 기준으로 정렬

result = [arr[0]] # 첫번째 회의

for i in range(1, len(arr)): # 두번째 회의부터 회의실 사용 가능한지 확인
    if result[-1][1] <= arr[i][0]: # 이전 회의의 종료시간보다 다음 회의의 시작시간이 늦으면
        result.append(arr[i]) # 회의실 사용가능
    
print(len(result)) # 회의실 사용팀 수 출력