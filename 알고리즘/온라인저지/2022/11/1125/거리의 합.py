import sys

input = sys.stdin.readline

input()
nums = list(map(int, input().rstrip().split()))
nums.sort()
result = 0
for num1 in nums:
    for num2 in nums:
        result += abs(num1-num2)
print(result)