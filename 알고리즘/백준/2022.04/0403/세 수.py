import copy
nums = list(map(int, input().split()))
original = copy.deepcopy(nums)
nums.sort()
A, B, C = nums[0], nums[1], nums[2]
# print(A, B, C)
ope = 1 # * or /
if A+B == C:
    ope = 0 # + or -
# print(ope)
# print(nums, original)
D, E, F = original[0], original[1], original[2]
result = ''
if not ope:
    if D+E == F:
        result = f'{D}+{E}={F}'
    elif E+F == D:
        result = f'{D}={E}+{F}'
    elif D-E == F:
        result = f'{D}-{E}={F}'
    elif E-F == D:
        result = f'{D}={E}-{F}'
else:
    if D*E == F:
        result = f'{D}*{E}={F}'
    elif E*F == D:
        result = f'{D}={E}*{F}'
    elif D//E == F:
        result = f'{D}/{E}={F}'
    elif E//F == D:
        result = f'{D}={E}/{F}'
print(result)