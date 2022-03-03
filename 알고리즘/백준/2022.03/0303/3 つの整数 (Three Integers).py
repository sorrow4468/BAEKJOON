nums = list(map(int, input().split()))

maxx = 0
result = 0

dp = [0] * 101

for i in range(len(nums)):
    dp[nums[i]] += 1
    if dp[nums[i]] > maxx:
        maxx = dp[nums[i]]
        result = nums[i]

print(result)