"""
까먹은 수의 위치
1. 맨 앞 or 맨 뒤
2. 중간

맨 앞 or 맨 뒤 일 경우 둘 중 아무거나 편한 거 출력
"""
nums = list(map(int, input().split()))
nums.sort()
diff = 1e9
for i in range(1, len(nums)):
    if nums[i] - nums[i-1] < diff:
        diff = nums[i] - nums[i-1]
in_middle = False
result = 0
for i in range(1, len(nums)):
    if nums[i] != nums[i-1] + diff:
        in_middle = True
        result = nums[i-1] + diff
if not in_middle:
    result = nums[-1] + diff
print(result)