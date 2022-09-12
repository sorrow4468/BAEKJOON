n = [int(input()) for _ in range(5)]
# print(n)
"""
- to -
- to +
0 to +
+ to +
"""
result = 0
if n[0] < 0 and n[1] < 0:
    result += abs(n[0]-n[1]) * n[2]
elif n[0] < 0 and n[1] > 0:
    result += abs(n[0])*n[2] + n[1]*n[4]
    result += n[3]
elif n[0] == 0 and n[1] > 0:
    result += n[3]
    result += n[1]*n[4]
elif n[0] > 0 and n[1] > 0:
    result += abs(n[0]-n[1])*n[4]
print(result)
