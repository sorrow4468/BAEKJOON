birth = list(map(int, input().split()))
now = list(map(int, input().split()))

olds = [0, 0, 0]

olds[2] = now[0] - birth[0]
olds[1] = olds[2] + 1
olds[0] = olds[2]

if (now[1] < birth[1]) or (now[1] == birth[1] and now[2] < birth[2]):
    olds[0] -= 1

for old in olds:
    print(old)