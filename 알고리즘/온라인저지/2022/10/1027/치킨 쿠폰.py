import sys

input = sys.stdin.readline

while True:
    try:
        N, K = map(int, input().rstrip().split())
        result = N
        stamp = N
        while stamp>=K:
            tmp = stamp//K
            stamp %= K
            result += tmp
            stamp += tmp
        print(result)
    except: break