arr = []
for i in range(int(input())):
    tmp = input()
    if tmp not in arr:
        arr.append(tmp)
arr.sort(key=lambda x:(len(x), x))
for a in arr:
    print(a)