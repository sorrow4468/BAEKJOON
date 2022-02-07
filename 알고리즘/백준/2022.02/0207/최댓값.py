maxx = 0
maxi = 0
maxj = 0

for i in range(9):
    line = list(map(int, input().split()))
    
    for j in range(9):
        if line[j] > maxx:
            maxx = line[j]        
            maxi, maxj = i, j

print(maxx)
print(maxi+1, maxj+1)
