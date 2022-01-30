x = [5, 6, 77, 45, 22, 12, 24]

i = 0
while True:
    if x[i]%2 == 0:
        x.remove(x[i])
    else:
        i += 1
    if i == len(x):
        break

print(x)