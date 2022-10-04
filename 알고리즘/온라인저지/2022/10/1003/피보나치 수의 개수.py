import sys

input = sys.stdin.readline

def check(fib):
    if A<=fib<=B: return 1
    else: return 0

while True:
    A, B = map(int, input().rstrip().split())
    if A == 0 and B == 0: break
    result = 0
    a, b = 1, 2
    result += check(a) + check(b)
    for _ in range(B-2): 
        if b>B: break
        a, b = b, a+b
        result += check(b)
    print(result)