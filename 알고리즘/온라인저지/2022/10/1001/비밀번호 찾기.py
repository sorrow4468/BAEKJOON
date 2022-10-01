import sys

input = sys.stdin.readline

N, M = map(int, input().rstrip().split())
dct = dict()
for n in range(N):
    site, password = input().rstrip().split()
    dct[site] = password
for m in range(M): print(dct[input().rstrip()])