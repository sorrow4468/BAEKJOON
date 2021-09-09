import sys
def input():
    return sys.stdin.readline()

def is_odd_or_even(N):
    if N%2:
        return True
    else:
        return False

N = int(input())
deck = list(range(1, N+1))
pop_or_keep = True # 버리기, False=살리기, 처음엔 버리면서 시작
while len(deck) > 1:
    odd_or_even = is_odd_or_even(len(deck))
    if odd_or_even:
        if pop_or_keep: # 홀수, 버리기
            deck = deck[1:len(deck)+1:2]
            pop_or_keep = False
        else: # 홀수, 살리기
            deck = deck[0:len(deck):2]
            pop_or_keep = True
    else:
        if pop_or_keep: # 짝수, 버리기
            deck = deck[1:len(deck)+1:2]
            pop_or_keep = True
        else: # 짝수, 살리기
            deck = deck[0:len(deck):2]
            pop_or_keep = False
print(*deck)