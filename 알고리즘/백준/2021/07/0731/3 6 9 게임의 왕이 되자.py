def three_six_nine(n):
    n = str(n) # 입력받은 숫자를 str로 변환
    tsn_list = "369" # 369를 확인하는 str값 설정
    result = "" # 초기 공백 결과값
    for num in n: # str로 바꿔준 n을 순회
        if num in tsn_list: # n의 각 숫자가 3,6,9일때
            result += "X" # 결과값에 박수 한 번
    if result == "": # 순회 다 해도 박수가 없으면
        result += n # 원본 숫자 출력
    return result # 결과값 반환

n = int(input()) # 숫자를 입력받고
for i in range(1, n+1): # 1부터 입력값까지 반복
    print(three_six_nine(i), sep = "") # 공백단위로 출력
