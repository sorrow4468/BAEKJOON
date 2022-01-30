l = []

for i in range(5):
    l.append(int(input()))

avg = sum(l)/5

print('입력된 값 {}의 평균은 {}입니다.'.format(l, avg))