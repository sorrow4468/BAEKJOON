table = [False] * 30

for _ in range(28):
    table[int(input()) - 1] = True

for i in range(30):
    if not table[i]:
        print(i+1)