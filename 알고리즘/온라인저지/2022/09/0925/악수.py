a=b=1
for _ in [0]*int(input()):a,b=b,(a+b)%10
print(a)