import sys

input = sys.stdin.readline

def gcd(a, b):
    while a%b: a, b = b, a%b
    return b

for _ in [0]*int(input().rstrip()):
    a, b = map(int, input().rstrip().split())
    G = gcd(a, b)
    print(G * (a//G) * (b//G))