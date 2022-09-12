A, B, V = map(int, input().split())
if (V-B)%(A-B):
    day = (V-B)//(A-B) + 1
else:
    day = (V-B)//(A-B)
print(day)