result = 0
for i in input().split(): result += int(i, 2)
print(bin(result)[2:])