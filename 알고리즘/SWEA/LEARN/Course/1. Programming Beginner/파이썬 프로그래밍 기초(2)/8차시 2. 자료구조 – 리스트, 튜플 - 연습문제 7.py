x = int(input())

s = set()

for i in range(1, x//2+1):
    if x%i == 0:
        s.add(i)
        s.add(int(x/i))

print(sorted(list(s)))