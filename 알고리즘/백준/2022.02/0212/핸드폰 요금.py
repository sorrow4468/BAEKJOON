N = int(input())

calls = list(map(int, input().split()))

Y = M = 0

for c in calls:
    Y += (c//30 + 1) * 10
    M += (c//60 + 1) * 15

if Y > M:
    print('M', min(Y, M))
elif M > Y:
    print('Y', min(Y, M))
else:
    print('Y M', Y)