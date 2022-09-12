arr = []

max_len = 0

for _ in range(5):
    tmp = input()
    arr.append(tmp)
    if len(tmp) > max_len:
        max_len = len(tmp)

for j in range(max_len):
    for i in range(5):
        try:
            print(arr[i][j], end='')
        except:
            pass



