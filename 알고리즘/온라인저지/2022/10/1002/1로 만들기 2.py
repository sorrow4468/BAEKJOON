import sys
from collections import deque

input = sys.stdin.readline

N = int(input().rstrip())
Q = deque()
Q.append([N])
result = []
while Q:
    now = Q.popleft()
    X = now[-1]
    if X == 1: result = now; break
    if X % 3 == 0: Q.append(now + [X//3])
    if X % 2 == 0: Q.append(now + [X//2])
    Q.append(now + [X-1])
print(len(result)-1)
print(*result)

"""
3으로 나누고, 2로 나누고, 1을 빼는
탐색기록 그 자체를 큐에 담으며 진행함
1에 도착했을 때의 탐색기록이 결과가 됨
스페셜저지 이므로 답은 아무거나 상관이 없음
해당 코드는 top-down DP코드이지만
1에서 출발하여 N까지 가는 bottom-up 코드를 짤 수도 있음
하지만 *연산보다 //연산이 시간이 조금 더 빠를지도..?
DP의 개념은 매우 단순함
"계산한 값을 기억했다가 다시 사용한다"
본디 다이나믹 프로그래밍이라는 이름 자체가
별 뜻이 없고, 만든 사람이 그냥 어그로성으로 붙인 이름이라고 함
한 번 계산된 값을 기록하여 재활용하는 알고리즘을 전부 DP로 봄
특징으로는, 계산된 값을 날리지 않고 들고 있는만큼
메모리가 많이 필요함
해당 코드는 수많은 리스트들이 Q에 들어가는 것처럼 보이지만
시간이 logN으로 빠른 이(二)분탐색보다 훨씬 빠른
코드상 삼(三)분탐색을 사용하므로 
저렇게 넘치게 Q에 append 하는 것처럼 보여도 메모리는 괜찮다
"""
# https://www.acmicpc.net/problem/12852