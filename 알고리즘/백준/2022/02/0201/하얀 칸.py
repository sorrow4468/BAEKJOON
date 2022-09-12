i = 1

result = 0

for _ in range(8):
    line = input()

    j = 1

    for l in line:
        if i%2:
            if j%2 and l == 'F':
                result += 1
        
        else:
            if not j%2 and l == 'F':
                result += 1
        
        j += 1
    
    i += 1

print(result)
        
    