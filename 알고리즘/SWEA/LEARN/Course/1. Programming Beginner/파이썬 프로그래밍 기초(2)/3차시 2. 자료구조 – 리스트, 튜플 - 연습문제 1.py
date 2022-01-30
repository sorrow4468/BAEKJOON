scores = [(90, 80), (85, 75), (90, 100)]

s = 0
avg = 0
i = 0

for score in scores:
    i += 1
    s = sum(score)
    avg = s/2
    print('{}번 학생의 총점은 {}점이고, 평균은 {}입니다.'.format(i, s, avg))
    