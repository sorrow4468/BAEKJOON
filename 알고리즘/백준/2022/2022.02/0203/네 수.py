nums1 = input().split()

result = 0

for i in range(0, 4, 2):
    result += int(nums1[i] + nums1[i+1])

print(result)