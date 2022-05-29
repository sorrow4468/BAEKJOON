N = int(input())
arr1 = list(map(int, input().split()))
for i in range(1, N+1):
    print(arr1[:i], sum(arr1[:i])//i, i)