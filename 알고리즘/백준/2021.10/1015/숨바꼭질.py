from collections import deque # deque의 메서드인 popleft()를 사용하기 위함

N, M = map(int, input().split())

result = 0

q = deque()
q.append((N, result)) # N부터 출발합니다

check = set() # +1 -1 *2 를 진행하면서 중복되는 숫자가 발견될 경우 
# q에 추가하는 것을 막기 위해 중복검사를 해주기 위한 set()

while q:
    if not N and not M or N == M: # 수빈이가 동생과 같은 위치에 있을 때
        break
    
    tmp = q.popleft() # BFS
    
    a = tmp[0] + 1
    b = tmp[0] - 1
    c = tmp[0] * 2
    cnt = tmp[1] + 1 # 수빈이가 이동하였고 1초가 지났습니다
    
    if M in (a, b, c): # 이동중 수빈이가 동생을 발견하였을 때
        result = cnt # 그 때의 시간을 저장
        break

    # 동생은 0부터 100000 사이에 있습니다, 범위를 벗어나면 동생을 찾을 수 없습니다
    if a not in check and 0<=a<=100000: # 간 적이 없고, 범위를 벗어나지 않으면
        q.append((a, cnt)) # 다음 가볼 곳에 추가
        check.add(a) # 가본 곳에 추가
    if b not in check and 0<=b<=100000:
        q.append((b, cnt))
        check.add(b)    
    if c not in check and 0<=c<=100000:
        q.append((c, cnt))
        check.add(c)

print(result)