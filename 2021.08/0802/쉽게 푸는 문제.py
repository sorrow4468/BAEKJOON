A, B = map(int, input().split())
numbers = []
for i in range(1, B+2):
    for j in range(i):
        numbers.append(i)
ls = []
for i in range(A-1, B):
    ls.append(numbers[i])

print(sum(ls))