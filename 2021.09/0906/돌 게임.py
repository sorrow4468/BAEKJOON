import sys
def input():
    return sys.stdin.readline()

N = int(input())
if N%2:
    print('SK')
else:
    print('CY')