N = int(input()) # 일정의 개수

dp = [0] * 365 # 일년치 달력

for n in range(N):
    S, E = map(int, input().split()) # 일정 입력

    for i in range(S-1, E): # 리스트를 365로 하였기 때문에 1일은 dp[0]
        # 시작도 S-1부터
        dp[i] += 1 # 일정이 있는 날 달력의 높이 하나 추가

# 연속된 일정단위로 만들어지는 직사각형의 넓이들의 합을 구해야 함
start = end = width = height = result = 0 # result는 출력값
counting = False # 연속된 일정인지 확인하기 위함

for i in range(365): # 일년동안
    if dp[i]: # 일정이 있는 날이면
        if not counting: # 연속된지 체크중이지 않으면
            counting = True # 체크중으로 변경
            start = i # 이 날 부터 연속된 일정이 시작
            height = dp[i] # 일정들의 높이의 최대값 초기화
        elif counting: # 연속된지 체크중이면
            if dp[i] > height: # 지금 보고 있는 일정의 높이가 더 높으면
                height = dp[i] # 높이 갱신
    else: # 일정이 없는 날이면
        if counting: # 체크중이면
            counting = False # 체크를 종료하고
            end = i # 전날까지가 연속된 일정
            width = end - start # 연속된 일정들의 직사각형의 가로는 (끝-시작)
            result += width * height # 결과값에 직사각형의 높이 저장
            width = height = 0 # 가로 세로 초기화

if dp[364] and counting: # 달력 마지막날이고, 체크중이라면
    end = 365 # 끝은 12월31일
    width = end - start # 가로
    result += width * height # 넓이를 결과값에 더해서

print(result) # 출력
    
