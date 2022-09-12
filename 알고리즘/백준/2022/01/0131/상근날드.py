burger = 2000
drink = 2000

for i in range(3):
    b = int(input())
    if b < burger:
        burger = b

for i in range(2):
    d = int(input())
    if d < drink:
        drink = d

result = burger + drink - 50

print(result)