import sys

input = sys.stdin.readline

N = int(input().rstrip())
dp = [1]*10
for i in range(1,N) :
    for j in range(1,10) :
        dp[j] += dp[j-1]
print(sum(dp)%10007)

"""
규칙은 찾았는데 구현하는게 막혔다
구현된 코드를 보고 이해는 가는데
어떻게 하면 이런 걸 코드로 쓸 수 있는지.. 신기하다

<참고한 링크>
https://jainn.tistory.com/91
"""

# https://www.acmicpc.net/problem/11057