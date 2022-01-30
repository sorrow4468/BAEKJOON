"""
테스트케이스 개수 C개
학생의 수 N명, 점수 N개
점수 N개의 평균
을 넘는 점수의 개수
를 전체 점수의 개수로 나눈 퍼센트
을 3자리까지 출력
을 테스트케이스 개수만큼"""

C = int(input()) # 테스트케이스 개수
for i in range(C): # 테스트케이스 개수만큼 순회하면서
    N_and_scores = list(map(int, input().split())) # 점수개수 N과 점수들을 입력받고
    N = N_and_scores[0] # N값을 잡아주고
    average = (sum(N_and_scores) - N) / N # 평균 구해주고
    count = 0 # 평균이상인 점수 개수 초기화
    for j in range(1, len(N_and_scores)): # 점수 리스트 순회하면서
        if N_and_scores[j] > average: # 평균이상인 점수 있으면
            count += 1 # 카운트 증가
    print(f'{(count / N) * 100:.3f}%') # 출력

# 입력받고 출력하고를 테스트케이스 개수만큼 반복하는 것이 가능하다
# 모든 값을 입력받고 저장해서 거기서 값을 꺼낼 필요가 없다
