""" 초기 풀이
N개의 숫자 중 소수는 몇개인가
소수인지 아는 법?
약수가 1과 자기 자신
주어질 수들은 1000이하 라는 조건
1000까지, 주어진 수들을, 이중순회 하면서
주어진 수를 1부터 주어진 수까지 나눌 때
주어진 수까지 나머지가 안 생기면 소수
중간에 나머지가 생기면(True) not소수
"""

# 최종 코드
N = int(input()) # 숫자 개수 입력받고
numbers = list(map(int, input().split())) # 숫자들 입력받고
count = 0 # 소수 개수를 셀 count 초기화
for number in numbers: # 입력받은 숫자들을 순회하면서
    for i in range(2, 1001): # 2부터 1000까지 나누면서 검사
        if number % i == 0: # 나머지가 없고
            if number == i: # number본인이면
                count += 1 # 소수이므로 count에 1 저장
            else: # 나머지는 0이지만 number본인이 아니라면
                break # 약수임

print(count) # 소수 개수 출력