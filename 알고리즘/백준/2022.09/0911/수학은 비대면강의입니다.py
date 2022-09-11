from copy import deepcopy

num = list(map(int, input().split()))
X, Y = deepcopy(num), deepcopy(num)
x, y = 0, 0
X[0] *= num[4]
X[1] *= num[4]
X[2] *= num[4]
X[3] *= num[1]
X[4] *= num[1]
X[5] *= num[1]
x = (X[2]-X[5])//(X[0]-X[3])
Y[0] *= num[3]
Y[1] *= num[3]
Y[2] *= num[3]
Y[3] *= num[0]
Y[4] *= num[0]
Y[5] *= num[0]
y = (Y[2]-Y[5])//(Y[1]-Y[4])
print(x, y)