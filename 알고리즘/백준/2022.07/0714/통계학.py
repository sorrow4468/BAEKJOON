from collections import Counter


N = int(input())
arr = [int(input()) for _ in range(N)]
arr.sort()
common = Counter(arr).most_common()
print(round(sum(arr)/N))
print(arr[N//2])
if len(common) > 1:
    if common[0][1] == common[1][1]:
        print(common[1][0])
    else:
        print(common[0][0])
else:
    print(common[0][0])
print(arr[-1]-arr[0])