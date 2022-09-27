import sys

input = sys.stdin.readline

def gcd(a, b):
    while a%b: a, b = b, a%b
    return b

N, M = map(int, input().rstrip().split(':'))
G = gcd(N, M)
print('{}:{}'.format(N//G, M//G))