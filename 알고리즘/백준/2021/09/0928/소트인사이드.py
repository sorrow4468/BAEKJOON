N = input()
a = [] # N을 쪼개어 담을 리스트
for n in N: # 입력받은 숫자는 아직 str문자형
    a.append(int(n)) # int로 형변환 하여 담기

a_sorted = [] # a에 담긴 숫자들을 정렬하여 담을 리스트
a_count = [0] * (max(a)+1) # N을 쪼개어 담은 a라는 리스트에 각 숫자들이 몇개씩 들어있는지 셀 것
# max(a)은, N의 각 자리수중 가장 큰 수를 의미하며
# +1은 각 숫자들의 개수를 세어 담을 때 리스트 맨 앞에 0을 의미함 -> 숫자와 인덱스가 일치함

for i in range(len(a)):
    a_count[a[i]] += 1 # 숫자와 인덱스가 일치, 해당 숫자의 개수를 세어줌

for i in range(len(a_count)-1, -1, -1): # 담겨있는 숫자의 개수들을 반복하면서
    # 문제에서는 역정렬을 요구하였음
    if a_count[i]: # 숫자의 개수가 하나라도 있으면
        for j in range(a_count[i]): # 카운트 한 개수만큼의 횟수를 반복하며
            print(i, end='') # 공백없이 출력하면 문제에서 요구하는 정답이 됨
