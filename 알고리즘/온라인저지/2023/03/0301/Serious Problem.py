result = 'yee'
input()
A = B = 0
for i in input():
    try:
        int(i)
        A += 1
    except:
        B += 1
if A > B:
    result = 2
elif A < B:
    result = 'e'
print(result)