for _ in range(int(input())):
    N, K = map(int, input().split())
    candies = list(map(int, input().split()))
    result = 0
    for candy in candies: result += candy//K
    print(result)