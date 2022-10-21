import sys

input = sys.stdin.readline

A, B = map(int, input().rstrip().split())
M = int(input().rstrip())
arr = list(map(int, input().rstrip().split()))[::-1]
num = 0
for i in range(M): num += A**i*arr[i]
base = 1
while base*B < num: base *= B
while base >= 1:
    print(num//base, end=' ')
    num, base = num%base, base//B