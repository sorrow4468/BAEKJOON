T = int(input())

for t in range(1, T+1):
    N, M = map(int, input().split())

    nums = list(map(int, input().split()))

    a = 99999999
    b = 0

    for i in range(len(nums)-M+1):
        tmp = sum(nums[i:i+M])
        a = min(a, tmp)
        b = max(b, tmp)
    
    print('#{} {}'.format(t, b-a))