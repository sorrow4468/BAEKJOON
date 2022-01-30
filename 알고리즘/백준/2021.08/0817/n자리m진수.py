n = 3
m = 5
list1 = [0] * n
for i in range(n-1, -1, -1):
    for j in range(m):
        list1[i] = j
        print(list1)