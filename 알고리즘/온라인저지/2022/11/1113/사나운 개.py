import sys

input = sys.stdin.readline

def bark(start, stop):
    i = 1
    while i+start < 1000:
        for j in range(i, i+start):
            if j < 1000: 
                dog[j] += 1
        i += start+stop

dog = [0]*1000
A, B, C, D = map(int, input().rstrip().split())
visitors = list(map(int, input().rstrip().split()))
bark(A, B); bark(C, D)
for visitor in visitors:
    print(dog[visitor])