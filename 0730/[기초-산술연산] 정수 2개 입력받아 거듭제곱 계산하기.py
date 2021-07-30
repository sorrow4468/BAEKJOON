# 두 변수를 입력받아서 각각 저장한다
# .split()이 하는 일이, 결국 input()받은 건 하나의 str인데
# 그걸 공백으로 쪼개서 각각 저장하는 기능을 한거다
a, b = input().split()
# **는 거듭제곱
c = int(a)**int(b) 
print(c)