"""
구하고자 하는 건 45분 전
분에 15분을 더하고
시간에 한시간을 빼고
60분을 넘기면 60을 빼주고
24시간을 넘기면 24를 빼주고
"""

H, M = map(int, input().split()) # 입력 받아서
M += 15 # 15분 더하고
H -= 1 # 1시간 빼고
if M >= 60: # 60분을 넘기면
    M -= 60 # 60빼주고 0분부터
    H += 1 # 1시간 더하고
if H >= 24: # 24시간 넘기면 0시부터
    H -= 24
if H == -1: # 계산을 마친 시간이 23시면
    H = 23 # 계산값인 -1을 23으로 덮어 씌우기
print(H, M) # 출력

