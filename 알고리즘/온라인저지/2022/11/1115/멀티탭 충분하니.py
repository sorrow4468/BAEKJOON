import sys

input = sys.stdin.readline

N, K = map(int, input().rstrip().split())
multi_taps = list(map(int, input().rstrip().split()))
result = 0
for multi_tap in multi_taps:
    result += (multi_tap+1)//2
print('YES' if result >= N else 'NO')