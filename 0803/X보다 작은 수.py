N, X = map(int, input().split()) # N은 왜준거지? 모르겠다
A = list(map(int, input().split())) # 수열을 입력받아서 리스트로 만들고
result = [] # 결과값을 초기화하고
for a in A: # 수열을 순회하면서
    if a < X: # X보다 작은 수는
        result.append(a) # 결과값에 추가
for res in result: # 결과값 수열을 순회하면서
    print(res, end=' ') # 띄어쓰기 간격으로 출력