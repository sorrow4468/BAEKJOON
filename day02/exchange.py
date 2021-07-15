#exchangeList > li.on > a.head.usd > div > span.value

"""
requests 불러온다.
"""
import requests
from bs4 import BeautifulSoup

url = "https://finance.naver.com/marketindex/"
response = requests.get(url).text # -> 응답 받은 문서를 문자열로 반환한다.
# bs4를 통해 파이썬이 읽을 수 있는 데이터 형으로 변경
# 변경하는 문서가 어떤 형태인지도 같이 작성해 줘야 한다.
# html.parser -> html 문서를 파이썬에서 읽을 수 있도록 만들어준다.

# 웹에서 파이썬으로 데이터를 옮겨오고
data = BeautifulSoup(response, "html.parser")

# 옮겨온 데이터에서 코스피지수를 추출해서
exchange = data.select_one("#exchangeList > li.on > a.head.usd > div > span.value")
# print(response)
# print(type(data))
# print(kospi)

# 현재의 코스피 지수는 ~~~ 입니다.

# 코스피 지수를 변수지정하여 값으로 출력
result = exchange.text
print(f"현재의 원/달러의 환율은 {result}입니다.")

