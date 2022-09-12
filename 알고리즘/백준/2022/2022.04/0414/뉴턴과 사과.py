people = list(map(int, input().split()))
X, Y, R = map(int, input().split())
if X in people:
    print(people.index(X)+1)
else:
    print(0)