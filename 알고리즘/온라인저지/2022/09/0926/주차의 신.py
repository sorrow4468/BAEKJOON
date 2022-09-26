import sys

input = sys.stdin.readline

for _ in range(int(input().rstrip())):
    input()
    parking = list(map(int, input().rstrip().split()))
    print((max(parking)-min(parking))*2)