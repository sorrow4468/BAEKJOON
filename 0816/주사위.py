N = int(input())
numbers = list(map(int, input().split()))
number = [min(numbers[0], numbers[5]), min(numbers[1], numbers[4]), min(numbers[2], numbers[3])]
    # 최소값을 도출해낼 수 있는 면 찾기
number.sort() # 사용할 숫자들 크기순으로 정리
A = number[0]
B = number[1]
C = number[2]
if N == 1: # 1*1일때는 그 주사위 자체이니까
    print(sum(numbers)-max(numbers)) # 가장 큰 수를 아랫면으로 놓은 값을 출력
else: # 1이 아니면
    print((((((N-1)*A)+B)*N)*4) + C*4 + (((N-2)*B)*4) + A*(N-2)*(N-2))
        # 최소값 출력
