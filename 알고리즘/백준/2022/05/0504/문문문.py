N = int(input())
M = int(input())
if N < 6:
    result = []
    door = [0, 1, 0, 1, 0, 1]
    door__reverse = [1, 0, 1, 0, 1, 0]
    if M == 0:
        for i in door[1:N]:
            result.append(i)
    else:
        for i in door__reverse[1:N]:
            result.append(i)
    for r in result:
        print(r)
else:
    print('Love is open door')