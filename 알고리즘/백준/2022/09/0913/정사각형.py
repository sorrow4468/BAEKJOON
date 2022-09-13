for _ in range(int(input())):
    dots = [tuple(map(int, input().split())) for __ in range(4)]
    x1, y1 = dots[0][0], dots[0][1]
    distance_pows = []
    for dot in dots[1:]:
        x2, y2 = dot[0], dot[1]
        distance_pow = abs(x1-x2)**2 + abs(y1-y2)**2
        distance_pows.append(distance_pow)
    flag = 1
    distance_pows.sort()
    if distance_pows[0] != distance_pows[1]:
        print(0)
    else:
        for self in dots:
            if not flag: break
            x1, y1 = self[0], self[1]
            tmp = []
            for other in dots:
                if self != other:
                    x2, y2 = other[0], other[1]
                    pow = abs(x1-x2)**2 + abs(y1-y2)**2
                    tmp.append(pow)
            tmp.sort()
            if tmp != distance_pows: flag = 0
        print(flag)