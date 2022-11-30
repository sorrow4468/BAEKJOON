N = int(input())
correct = [1, 2, 3, 4, 5]
for answer in range(1, N+1):
    arr = list(map(int, input().split()))
    if arr[:5] != correct: continue
    if arr[5:] != correct: continue
    print(answer)