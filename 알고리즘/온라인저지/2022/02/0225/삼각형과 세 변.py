while True:
    A, B, C = map(int, input().split())
    if A+B+C == 0:
        break

    result = 'Scalene'

    if A+B+C == max(A, B, C) * 2:
        result = 'Invalid'
    
    nums = set([A, B, C])

    if len(nums) == 2:
        temp = [A, B, C]
        temp.sort()
        if temp[2] - temp[0] >= temp[1]:
            result = 'Invalid'
        else:
            result = 'Isosceles'
    elif len(nums) == 1:
        result = 'Equilateral'

    print(result)
