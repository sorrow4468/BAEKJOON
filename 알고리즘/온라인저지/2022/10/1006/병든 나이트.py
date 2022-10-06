import sys

input = sys.stdin.readline

N, M = map(int, input().rstrip().split())
result = 0
if N == 1: result = 1
elif N == 2: result = min(4, (M+1)//2)
else: # N >= 3
    if M < 7: result = min(4, M)
    else: result = M-2
print(result)

"""
<참고한 링크>
https://pacific-ocean.tistory.com/354
"""

# https://www.acmicpc.net/problem/1783