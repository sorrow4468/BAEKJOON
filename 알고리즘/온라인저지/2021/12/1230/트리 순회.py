N = int(input())

tree = dict()

for n in range(N):
    temp = input().split()
    tree.update({temp[0]:temp[1:]})

print(tree)