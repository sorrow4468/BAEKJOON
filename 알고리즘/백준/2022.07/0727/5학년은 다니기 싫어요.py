N, A, B = map(int, input().split())
L = 8-N # left : 남은 학기
LA = 66-A # 남은 전공학점
LB = 130-B # 남은 총학점
result = 'Nae ga wae'
C = [tuple(map(int, input().split())) for _ in range(10)]
for l in range(L):
    # 한 학기 최대 이수 6과목 18학점
    LC = 6 # left credits : 남은 이번학기 수강가능 학점
    tmp_a = C[l][0]
    LA -= tmp_a * 3
    LC -= tmp_a
    tmp_b = C[l][1]
    if LC >= tmp_b:
        LB -= tmp_a*3 + tmp_b*3
    else:
        LB -= tmp_a*3 + LC*3
    if LA<=0 and LB<=0:
        result = 'Nice'
print(result)