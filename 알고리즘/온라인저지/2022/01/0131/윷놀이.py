status = {
    3: 'A',
    2: 'B',
    1: 'C',
    0: 'D',
    4: 'E',
}

for t in range(3):
    yoot = sum(list(map(int, input().split())))

    print(status[yoot])
