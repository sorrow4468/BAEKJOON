import sys

input = sys.stdin.readline

N = int(input())
odd = False
if N%2: N += 1; odd = True
A = N//2 + 1
print(A**2 - A if odd else A**2)