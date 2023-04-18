H, W = ord('L')-65+1, 4
for _ in range(int(input())):
    N, M = map(int, input().split())
    result = -1
    if N>=H and M>=W:
        result = (H-1)*M+4
    print(result)