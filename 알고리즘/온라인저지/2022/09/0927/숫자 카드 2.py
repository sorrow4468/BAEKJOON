import sys

input = sys.stdin.readline

input().rstrip()
cards = list(map(int, input().rstrip().split()))
count = dict()
for card in cards:
    try: count[card] += 1
    except: count[card] = 1
input().rstrip()
for i in list(map(int, input().rstrip().split())):
    try: print(count[i], end=' ')
    except: print(0, end=' ')