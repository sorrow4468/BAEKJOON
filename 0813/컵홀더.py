"""
컵홀더 개수 = 좌석수 - 커플석 개수 + 1
리스트 받아서 while문으로 리스트 탐색
"""
N = int(input())                        # 좌석 수
seats = list(input())                   # 좌석 리스트
i = 0                                   # 좌석 리스트 탐색 인덱스
couple_go_to_hell = 0                   # 커플석 개수 카운트
while i != len(seats):                  # 좌석 탐색 반복
    if seats[i] == 'L':                 # 자리가 커플석이면
        couple_go_to_hell += 1          # 커플석 카운트
        i += 1                          # 옆칸도 커플석이니까 한 칸 패스
    i += 1                              # 다음 좌석으로 ㄱㄱ
if N <= N - couple_go_to_hell + 1:      # 커플석이 없으면
    print(N)                            # 그냥 좌석수 출력
else:                                   # 커플석이 많아서 컵홀더가 좌석보다 적으면
    print(N - couple_go_to_hell + 1)    # 컵홀더개수 출력