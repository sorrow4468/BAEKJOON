import sys
def input():
    return sys.stdin.readline()

cnt = input()
measures = list(map(int, input().split()))
print(max(measures) * min(measures))