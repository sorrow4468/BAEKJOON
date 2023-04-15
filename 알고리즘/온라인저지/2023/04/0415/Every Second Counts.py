times = []
for _ in range(2):
    h, m, s = map(int, input().split(' : '))
    times.append((h*60+m)*60+s)
a, b = times
if b < a: b += 24*60*60
print(b-a)