N, S = map(int, input().split())

arr = list(map(int, input().split()))

n = len(arr)

cnt = 0 # 부분집합의 합이 S가 될 때마다 +1

# 비트연산 "<<"를 통해 부분집합을 구해줄 것
for i in range(1<<n): # 2의 len(arr)승 -> arr의 부분집합의 개수
    tmp = [] # 부분집합 초기화
    for j in range(n): 
        if i&(1<<j): # 1<<j == arr에서 j번째 원소를 의미
            # 만약 i의 비트가 11100이면
            # tmp == 리스트의 0번째, 1번째, 2번째 원소를 가지는 arr의 부분집합
            tmp.append(arr[j]) # 해당 부분집합의 원소를 부분집합에 추가
    if sum(tmp) == S:
        if len(tmp) == 0: # 공집합은 예외처리
            pass
        else: # 
            cnt += 1

print(cnt) # 출력
            
