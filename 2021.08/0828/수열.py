import sys
N = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))
cnt = 1
result = 1
# 증가할 때 따로, 감소할 때 따로, 두번 돌려주는 코드
for i in range(len(nums)-1):
    if nums[i] >= nums[i+1]:
        cnt += 1
    else:
        cnt = 1
    if result < cnt:
        result = cnt

cnt = 1
for i in range(len(nums)-1):
    if nums[i] <= nums[i+1]:
        cnt += 1
    else:
        cnt = 1
    if result < cnt:
        result = cnt
print(result)