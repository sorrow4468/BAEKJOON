import sys

input = sys.stdin.readline

N, M = map(int, input().rstrip().split())
print((str(N)*N)[:M])

"""
<참고한 링크>
https://hongku.tistory.com/268
"""

# https://www.acmicpc.net/problem/11944