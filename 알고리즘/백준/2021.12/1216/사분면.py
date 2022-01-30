N = int(input())

quadrant = [0 for _ in range(5)]

for n in range(N):
    x, y = map(int, input().split())

    if x == 0 or y == 0:
        quadrant[4] += 1
    elif x > 0 and y > 0:
        quadrant[0] += 1
    elif x < 0 and y > 0:
        quadrant[1] += 1
    elif x < 0 and y < 0:
        quadrant[2] += 1
    elif x > 0 and y < 0:
        quadrant[3] += 1

for i in range(5):
    if i == 4:
        print('AXIS: {}'.format(quadrant[i]))
        break

    print('Q{}: {}'.format(i+1, quadrant[i]))
