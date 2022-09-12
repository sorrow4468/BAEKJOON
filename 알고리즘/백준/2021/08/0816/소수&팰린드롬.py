"""
N보다 큰 수를 하나씩 올려가면서
소수들로 나눠서 나머지가 있으면서 소수본인과 같아지면 소수
2~N까지의 소수들을 먼저 리스트에 추가
N+1이 소수인지 보고 소수이면 리스트에 추가
소수일 때 팰린드롬인지 보고
팰린드롬이면 출력
"""
import sys
N = int(sys.stdin.readline())

                                    # 1003001까지 에라토스테네스의 체로 소수 전부 골라내기
n = 1003003                         # 조금 편법이긴 한데
                                    # 최대값이 1003001이라는 걸 계산해서 먼저 알아냄
a = [False,False] + [True]*(n-1)
primes=[]
for i in range(2,n+1):
  if a[i]:
    primes.append(i)
    for j in range(2*i, n+1, i):
        a[j] = False

prime_palindrome = 0                # 소수팰린드롬 초기값
while True:
    if str(N) == str(N)[::-1]:      # 팰린드롬이고
        if N in primes:             # 소수이면
            prime_palindrome = N    # 소수팰린드롬
    if prime_palindrome:            # 값을 찾았다면
        print(prime_palindrome)     # 출력하고
        break                       # while문 종료
    N += 1                          # 다음 숫자 탐색

