V = int(input())

votes = input()

avote = 0
bvote = 0

for v in votes:
    if v == 'A':
        avote += 1
    else:
        bvote += 1

if avote > bvote:
    print('A')
elif bvote > avote:
    print('B')
else:
    print('Tie')