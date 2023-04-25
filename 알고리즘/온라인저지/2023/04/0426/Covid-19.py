result = 'Yellow'
p = int(input())
q = int(input())
if p<=50 and q<=10:
    result = 'White'
elif q>30:
    result = 'Red'
print(result)