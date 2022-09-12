L, C = map(int, input().split())
arr = list(input().split())

n = len(arr)
result = []
for i in range(1<<n): # 모든 암호(부분집합)들 중에서
    tmp = []
    for j in range(n):
        if i&(1<<j):
            tmp.append(arr[j])
    if len(tmp) == L: # 길이가 L이고
        if ('a' in tmp) or ('e' in tmp) or ('i' in tmp) or ('o' in tmp) or ('u' in tmp): # 모음이 하나이상 있고
            count = 0
            for tm in tmp:
                if tm in 'bcdfghjklmnpqrstvwxyz': # 자음이
                    count += 1
            if count >= 2: # 두개 이상일 때
                tmp.sort() # 정렬해서
                tmp2 = ''
                for t in tmp:
                    tmp2 = tmp2 + t # 단어로 만들어서
                result.append(tmp2) # 추가
result.sort() # 추가한 값들을 정렬
for res in result:
    print(res) # 출력