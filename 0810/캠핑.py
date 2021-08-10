"""
L P V
result = (V//P) * L"""
count = 0
while True:
    L, P, V = map(int, input().split()) # 각각 변수를 입력받고
    count += 1 # Case count: ? 출력해줄 count변수
    if L + P + V == 0: # 마지막항으로 0 0 0 들어오면
        break # 종료
    C = V - ((V//P) * P) # 다 나눠주고 나머지 더할 상수 C
    if C > L: # C가 L보다 크면
        C = L # L보다 클 때 모두 다 C로 치환
    print(f'Case {count}: {((V//P) * L) + C}') # 테스트케이스마다 결과값 출력
    