def plus_or_multiply(A, B):
    if A == B: # 등차
        Q = nums[1]-nums[0]
        result = nums[-1]+Q
    else: # 등비
        Q = nums[1]//nums[0]
        result = nums[-1]*Q
    return result

N = int(input())
nums = [int(input()) for _ in range(N)]
A, B = 0, 0
if N == 3:
    A, B = nums[0]+nums[-1], nums[1]*2
else:
    A, B = nums[0]+nums[-1], nums[1]+nums[-2]
print(plus_or_multiply(A, B))