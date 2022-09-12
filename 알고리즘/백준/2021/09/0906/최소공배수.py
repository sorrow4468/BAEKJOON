import sys
def input():
    return sys.stdin.readline()

T = int(input())
for t in range(T):
    A, B = map(int,input().split())
    C, D = A, B
    while A % B != 0:
        A, B = B, A % B
    print(B * (C//B) * (D//B))

