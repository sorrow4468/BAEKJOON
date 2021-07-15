# 터미널 단축키 : Ctrl + `
# 숫자
# int는 양의정수 + 0 만 가능
number = 3
print(type(number))

# 문자열
string = "문자열"
print(type(string))

# boolean
boolean = True
print(type(boolean))

# 형변환
string_number = "58"
# 문자열을 숫자로 바꾼다음 타입을 출력한다.
print(int(string_number) + 5)
print(type(int(string_number)))
print(type(string_number))

# f-string / string interpolation
name = "홍길동"
# 문자열 앞에 f를 붙이고, 변수를 넣고 싶은 곳에 {}
print(f"{name}입니다. 반갑습니다.")

"""
여러줄 주석입니다.
리스트
"""
# #주석은 한줄만 주석
# 여러줄 주석 달 때
# 주석
# 주석 하지 말고
"""
이렇게
묶어서
주석을 달 수 있다
"""

print("\nNext Step")
# 리스트 선언
my_list = ["java", "python"]

# 리스트 원소 접근
# List[index]
print(my_list[0])

# 리스트 원소 변경
# my_list의 첫번째 요소를 "django"라는 문자열로 바꾸고 싶다. 어떻게 해야할까?
# my_list의 첫번째 요소에 접근 후 변경
my_list[0] = "django"
print(my_list)

# 리스트 길이
# length -> len()함수
print(len(my_list))

"""
딕셔너리
"""

print("\nNext Step")
# 딕셔너리 선언
my_info = {
    "name": "이정원",
    "age": 27
}
print(my_info)

# 딕셔너리 원소 접근
print(my_info["name"])
# 가지고 있지 않은 key로 접근하면 keyerror가 발생한다.
# print(my_info["location"])

# 딕셔너리는 원소 접근 방법이 2가지가 있다.
# 딕셔너리가 가지고 있는 get함수
# get을 통해 없는 키값을 가지고 오면 None으로 출력한다.
print(my_info.get("name"))

# 딕셔너리 원소 변경
my_info["name"] = "홍길동"
print(my_info)

"""
딕셔너리 실습
"""
print("\nNext Step")

coin = {
    'BTC': {
        'opening_price': '44405000',
        'closing_price': '38806000',
        'min_price': '36640000',
        'max_price': '44999000',
        'prev_closing_price': '44404000',
        'fluctate_24H': '-7463000',
        'fluctate_rate_24H': '-16.13',
    },
    'ETH': {
        'opening_price': '1458000',
        'closing_price': '1229000',
        'min_price': '1100000',
        'max_price': '1490000',
        'prev_closing_price': '1458000',
        'fluctate_24H': '-275000',
        'fluctate_rate_24H': '-18.28',
    },
    'XRP': {
        'opening_price': '364.5',
        'closing_price': '311.9',
        'min_price': '284.2',
        'max_price': '372.7',
        'prev_closing_price': '364.2',
        'fluctate_24H': '-90.6',
        'fluctate_rate_24H': '-22.51',
    },
}

# 2-1. 코인의 정보에서 BTC의 최대 가격을 출력하시오.
print("BTC의 최대가격:", coin['BTC']["max_price"])

# 2-2. BTC의 시가와(opening price) XRP의 시가를 더한 결과를 출력하시오.
total_price = int(coin['BTC']["opening_price"]) + float(coin['XRP']["opening_price"])
print("BTC의 시가와(opening price) XRP의 시가를 더한 결과:", total_price)

print("\nNext Step")
