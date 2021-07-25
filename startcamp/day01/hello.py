# greeting 이라는 변수에 "안녕하세요" 라는 문자를 할당한다.
greeting = "안녕하세요"

# greeting변수가 담고 있는 값을 출력한다.
# print(greeting)
# 주석처리 -> Ctrl + /

print("\nNext Step")
# 반복문을 통해서 한번 인사를 여러번 하도록 해보자.
# while 조건:
# 조건을 만들기 위해서
count = 0
# count가 4 미만인 동안만 반복 실행
# while은 종료 조건이 중요한데
# 무한반복을 탈출하는 단축키는 Ctrl + C
while count < 4:
    # greeting을 출력한다.
    print(greeting)
    count += 1

print("\nNext Step")
# for문으로도 반복 해보고 싶은데...
# for문은... list를 넣어야 한다고 했는데...?
# 리스트랑 greeting이랑 무슨 상관이지...
# 0부터 n-1까지의 숫자들을 만들어주는 range()
# range(5) -> 0, 1, 2, 3, 4
for i in range(5):
    print(greeting)
