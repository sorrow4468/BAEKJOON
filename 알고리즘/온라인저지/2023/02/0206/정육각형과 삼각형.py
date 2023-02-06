import math

L = int(input())
cos_30 = math.cos(math.radians(30))
cos_60 = math.cos(math.radians(60))
result = L**2 * cos_30 * cos_60
print(f'{result:.9f}')  