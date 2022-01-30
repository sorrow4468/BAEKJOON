s = set()

for i in range(1, 21):
    if i%3 or i%5:
        s.add(i*i)

print(sorted(list(s)))