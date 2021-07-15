# while문이 종료할 수 있도록 종료조건이 필요함
dust = [59, 24, 102, 45, 64]
n = 0
while n<3:
    print(dust[n])
    n += 1

# 정해진 범위를 반복하기에 종료조건이 필요 없음
print("\n")
for i in dust:
    print(i)