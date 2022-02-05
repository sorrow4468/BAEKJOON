dwarfs = []

for _ in range(9):
    dwarfs.append(int(input()))

sum_dwarfs = sum(dwarfs)

fakes_idx = []

for i in range(8):
    temp = sum_dwarfs - dwarfs[i]

    for j in range(i, 9):
        if temp - dwarfs[j] == 100:
            fakes_idx.append(i)
            fakes_idx.append(j)
            break
    
    if fakes_idx:
        break

for i in range(9):
    if i not in fakes_idx:
        print(dwarfs[i])
