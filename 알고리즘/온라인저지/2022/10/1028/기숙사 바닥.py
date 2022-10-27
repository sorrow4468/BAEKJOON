import sys

input = sys.stdin.readline

R, B = map(int, input().rstrip().split())
divisors = []
for i in range(1, int((R+B)**0.5+1)):
    if not (R+B)%i:
        divisors.append((i, (R+B)//i))
for divisor in divisors:
    W, L = divisor
    red = 0
    if W > 1:
        red += (W+L-2)*2
    else: red = L
    if red == R:
        print(L, W)
        break