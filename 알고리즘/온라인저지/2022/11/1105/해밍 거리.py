import sys

input = sys.stdin.readline

for _ in range(int(input().rstrip())):
    nums = [input().rstrip() for i in range(2)]
    result = 0
    for i in range(len(nums[0])):
        if nums[0][i] != nums[1][i]:
            result += 1
    print('Hamming distance is {}.'.format(result))