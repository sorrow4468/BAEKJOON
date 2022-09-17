A = int(input())
B = int(input())
C = int(input())
D = int(input())
P = int(input())

result = 0

XP = A * P

YP = B

if P > C:
    YP += (P-C) * D

result = min(XP, YP)

print(result)