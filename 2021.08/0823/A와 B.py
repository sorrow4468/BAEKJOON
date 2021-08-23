S = list(input())
T = list(input())
result = 0
# A를 추가하거나, 뒤집고 B를 추가하는 두가지만 가능
# 뒤집어서 생각하면
# T에서 A를 빼거나, B를 빼고 뒤집어가면서 S와 일치하는지 확인
while True:
    if S == T: # 만들 수 있으면 
        result = 1 # 1
        break
    if T[-1] == 'A': # 맨 뒷글자가 A면
        T.pop() # 빼고
        if not T: # 다 빼서 T가 []가 되면
            break # 종료
    elif T[-1] == 'B': # 맨 뒷글자가 B면
        T.pop() # 빼고
        if not T: # T == []
            break # 종료
        T = T[::-1] # 뒤집고

print(result)