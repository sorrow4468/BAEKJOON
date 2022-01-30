import sys

M = int(input())

S = set() # set자료형으로 생성
# add과정에서 x가 이미 있는 경우 무시할 것이기 때문에 데이터들은 절대 중복될 수 없다
# 따라서 순서를 지니지 않는 set자료형으로 만들어서 시간초과를 회피
# 추가하고 제거하는 과정에서 list자료형의 append와 remove혹은 pop을 쓰는 것 보다
# set자료형의 add와 discard를 쓰는 것이 빠르다

for m in range(M):
    orders = sys.stdin.readline().split()

    if len(orders) == 1: # all이 명령어로 들어왔을 때
        order = orders[0] # add remove check toggle all empty등, 명령어
    else: # all을 제외한 명령어들일 때
        order = orders[0] # 명령어
        num = int(orders[1]) # 목적 숫자 x

    if order == 'add':
        S.add(num) # list자료형의 append와 같음
    elif order == 'remove':
        S.discard(num) # list자료형의 remove혹은 pop와 같음
    elif order == 'check':
        if num in S:
            print(1)
        else:
            print(0)
    elif order == 'toggle':
        if num in S:
            S.discard(num)
        else:
            S.add(num)
    elif order == 'all':
        S = set([i for i in range(1, 21)]) # 1~20까지 전부 채워진 set로 리셋
    else:
        S = set() # set를 초기화

# 추가적으로 해당 문제는 메모리도 많이 적은 편이라
# python의 경우 평소처럼 pypy3로 제출하면 메모리부족으로 오답처리 된다
