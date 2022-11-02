while True:
    nums = list(map(int, input().split()))
    if nums[0] == -1: break
    result = 0
    arr = [0]*101
    for num in nums[:len(nums)-1]:
        if not arr[num]: arr[num] = 1
    for num in nums[:len(nums)-1]:
        if num*2 <= 100 and arr[num*2]: 
            result += 1
    print(result)