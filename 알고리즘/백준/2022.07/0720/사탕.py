T = int(input())
for t in range(T):
    J, N = map(int, input().split())
    boxes = []
    for n in range(N):
        R, C = map(int, input().split())
        boxes.append(R*C)
    boxes.sort(reverse=True)
    result = 0
    for b in boxes:
        result += 1
        J -= b
        if J <= 0: 
            break
    print(result)
