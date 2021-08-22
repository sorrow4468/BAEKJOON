dwarf = []
for n in range(9):
    dwarf.append(int(input()))
dwarf.sort()
all_dwarf = sum(dwarf)
found = False
for i in range(8):
    for j in range(i+1, 9):
        if all_dwarf - dwarf[i] - dwarf[j] == 100:
            dwarf.pop(dwarf.index(dwarf[i]))
            dwarf.pop(dwarf.index(dwarf[j-1]))
            found = True
            break
    if found:
        break
for dwa in dwarf:
    print(dwa)