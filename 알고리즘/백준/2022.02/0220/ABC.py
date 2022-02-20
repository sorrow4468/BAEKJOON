nums = list(map(int, input().split()))
nums.sort()

for i in input():
    if i == 'A':
        print(nums[0])
    elif i == 'B':
        print(nums[1])
    elif i == 'C':
        print(nums[2])