T = int(input())
for t in range(T):
    N = int(input())
    nums = list(map(int, input().split()))
    print(min(nums), max(nums))