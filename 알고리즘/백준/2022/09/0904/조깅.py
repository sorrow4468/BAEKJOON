N, T = map(int, input().split())
runner = [tuple(map(int, input().split())) for _ in range(N)]
stack = []
cnt = 1
for r in runner[::-1]:
    tmp = r[0] + (r[1]*T)
    if stack and tmp < stack[-1]:
        cnt += 1
    if stack and tmp >= stack[-1]:
        stack.append(stack[-1])
    else:
        stack.append(tmp)
    print(tmp, stack)
print(cnt)

"""
맨 선두에 있는 주자부터 이동한다
당연히 맨 선두 주자는 하나의 그룹이 된다
그 다음 주자를 이동한다
그 다음 주자의 최고 이동거리가 선두주자보다
같거나 클 경우 한 그룹으로 붙는다
아닐 경우 다른 그룹이 된다
"""