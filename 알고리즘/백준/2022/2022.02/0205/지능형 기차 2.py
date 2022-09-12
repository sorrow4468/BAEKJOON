maxx = 0
in_train = 0

for _ in range(10):
    l, b = map(int, input().split())
    in_train += b-l
    if in_train > maxx:
        maxx = in_train

print(maxx)

