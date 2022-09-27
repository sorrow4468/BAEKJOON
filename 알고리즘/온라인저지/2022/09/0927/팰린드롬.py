import sys
from itertools import combinations as comb

input = sys.stdin.readline

for _ in [0]*int(input().rstrip()):
    K = int(input().rstrip())
    words = [input().rstrip() for _ in [0]*K]
    word_comb = list(comb(words, 2))
    for a, b in word_comb:
        A, B = a+b, b+a
        if A == A[::-1]:
            print(A)
            break
        if B == B[::-1]:
            print(B)
            break
    else: print(0)
