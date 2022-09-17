def RSP(player1, player2):
    result = 0
    if player1 == 'R':
        if player2 == 'R':
            result += 1    
        elif player2 == 'S':
            result += 2
    elif player1 == 'S':
        if player2 == 'S':
            result += 1
        elif player2 == 'P':
            result += 2
    elif player1 == 'P':
        if player2 == 'R':
            result += 2
        elif player2 == 'P':
            result += 1
    return result


R = int(input())
SG = list(input()) # 상근
N = int(input())
friend = [] # 친구들
for n in range(N): 
    friend.append(list(input()))
result1 = result2 = 0
for i in range(R):
    for f in friend: # 상근이의 점수
        result1 += RSP(SG[i], f[i])
    maxx = 0 # 최대점수 초기화
    for j in 'RSP': # 최대점수 구하기
        tmp = 0
        for f in friend:
            tmp += RSP(j, f[i])
        if tmp > maxx:
            maxx = tmp
    result2 += maxx
print(result1)
print(result2)