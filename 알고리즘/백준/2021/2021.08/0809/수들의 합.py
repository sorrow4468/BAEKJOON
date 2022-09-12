import sys
S = int(sys.stdin.readline()) # S값 입력받고
N = 0 # 더해줄 N값 초기화
count = 0 # 최대 개수 초기화
while True: # while문 반복하면서
    N += 1 # 1부터 S값에서 빼기 시작
    if N > S: # 종료조건
        break
    S -= N # S에서 N을 빼주면서 S를 N보다 작게 만들때까지
        # 수의 개수를 
    count += 1 # 세어주고
print(count) # 출력
