N = int(input())
arr = set()
for n in range(1, int(N**0.5)+1):
    if not N%n:
        arr.add(n)
        arr.add(N//n)
print(sum(arr)*5-24)