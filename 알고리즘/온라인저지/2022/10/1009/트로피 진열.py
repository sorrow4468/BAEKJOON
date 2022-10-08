from audioop import reverse
from re import A
import sys

input = sys.stdin.readline

def check(arr):
    result = 1
    biggest = arr[0]
    for a in arr:
        if a>biggest:
            biggest = a
            result += 1
    return result

N = int(input().rstrip())
arr = [int(input().rstrip()) for _ in range(N)]
print(check(arr))
print(check(arr[::-1]))