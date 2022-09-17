age = [[] for _ in range(201)]
T = int(input())
for t in range(T):
    member = input().split()
    age[int(member[0])].append(member)
for a in age:
    if a:
        for i in a:
            print(*i)