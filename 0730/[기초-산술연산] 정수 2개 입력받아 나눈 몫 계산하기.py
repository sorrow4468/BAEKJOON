# 각각 입력받아서 split으로 각각 저장해주고
a, b = input().split()
# 무조건 각각 int 적용해줘야 한다
# 입력받는 과정에서 하려니까 에러가 나버리네
a = int(a)
b = int(b)
print(a//b)