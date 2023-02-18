import sys

input = sys.stdin.readline

S = input().strip()
l = len(S)

if S == S[0]*l: print(-1)
elif S == S[::-1]: print(l-1)
else: print(l)