# 변수 세 개 받아서
# 공백으로 쪼개서
# int로 바꿔주고
# map으로 각각 저장해준다
a, b, c = map(int, input().split())
d = a + b + c
e = round(d / 3, 3)
# f"{:.?f}"로 소수점 아래 자리수 고정시킬 수 있다
print(f"{d} {e:.2f}")