dishes = input()

height = 10

prev_dish = dishes[0]

for i in range(1, len(dishes)):  
    if dishes[i] == prev_dish:
        height += 5
    else:
        height += 10
        prev_dish = dishes[i]
    
print(height)
