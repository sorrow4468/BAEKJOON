import sys

input = sys.stdin.readline

for t in range(1, int(input().rstrip())+1):
    P, Q = map(int, input().rstrip().split())
    a, b = 1, 1
    for _ in range(P-2): a, b = b, (a+b)%Q
    if Q == 1: b = 0
    print('Case #{}: {}'.format(t, b))