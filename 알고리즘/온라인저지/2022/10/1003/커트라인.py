import sys

input = sys.stdin.readline

N, K = map(int, input().rstrip().split())
print(sorted(list(map(int, input().rstrip().split())), reverse=True)[K-1])