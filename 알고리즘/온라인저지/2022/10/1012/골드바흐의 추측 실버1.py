import sys

input = sys.stdin.readline

n = int(1e6)
a = [False,False] + [True]*(n-1)
for i in range(2, 1001):
    if a[i]:
        for j in range(2*i, n+1, i):
            a[j] = False
while True:
    N = int(input().rstrip())
    if N == 0: break
    for i in range(3, n):
        if a[N-i] and a[i]:
            print('{} = {} + {}'.format(N, i, N-i))
            break
    else: print("Goldbach's conjecture is wrong.")

"""
에라토스테네스의 체를 만드는 과정에서 
primes를 만들기 위해 append 하는 부분을 없앴다
소수판정 테이블인 a만 활용하여 시간초과를 회피하였다
결론적으로 골드바흐의 추측은 백만 이하 모든 짝수에 적용이 가능하다
"""

# https://www.acmicpc.net/problem/6588