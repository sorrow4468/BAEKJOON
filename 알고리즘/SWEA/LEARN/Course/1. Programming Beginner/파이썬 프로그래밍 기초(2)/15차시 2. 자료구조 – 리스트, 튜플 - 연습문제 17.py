import math
from math import pi

x = list(map(int, input().split(', ')))

for i in x:
    if i == x[-1]:
        print(round(2*pi*i, 2))
    else:
        print(round(2*pi*i, 2), end=', ')