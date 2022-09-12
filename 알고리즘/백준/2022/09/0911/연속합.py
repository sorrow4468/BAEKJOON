N = int(input())
nums = list(map(int, input().split()))
result = [nums[0]]
for i in range(len(nums)-1):
    result.append(max(result[i]+nums[i+1], nums[i+1]))
print(max(result))

"""
한 시간을 머리를 박았는데
접근도 못하고
답지를 봤더니 이렇게 허무할 줄은 몰랐다
실패요인은
DP라는 태그를 보고 그 계산값들을 저장하면서
들고 간다는 것 까지는 이해하였지만
어떻게 들고 가는지, 그 과정을 이해하지 못하였다
result[i] : min(여기까지 끌고온 연속합, i번째 값)
result[i]+nums[i+1] : 구해온 연속합에 다음 수를 더한 값
nums[i+1] : 현재 값
result에는, 최대값이 될 수 있는
구한 연속값들이 모두 들어있고
그 중에 최대값을 max(result)를 통해 출력하는 문제였다
"""