W, H, X, Y, P = map(int, input().split())
LB = [X, Y] # left bottom
RT = [X+W, Y+H] # right top
R = H//2
result = 0
for p in range(P):
    tmp = list(map(int, input().split()))
    square = True
    for i in range(2):
        if tmp[i] < LB[i] or tmp[i] > RT[i]:
            square = False
    if square:
        result += 1
    x, y = tmp
    if (abs(x-X)**2 + abs(y-(Y+R))**2)**0.5 <= R and not square:
        result += 1
    elif (abs(x-(X+W))**2 + abs(y-(Y+R))**2)**0.5 <= R and not square:
        result += 1
print(result)