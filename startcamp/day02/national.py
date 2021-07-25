import requests

name = "david"
url = f"https://api.nationalize.io/?name={name}"
response = requests.get(url).json()
print(response)
print(type(response))
print(type(response["country"]))
country = response["country"][0]["country_id"]
probability = round(response["country"][0]["probability"] * 100, 2)
print(type(probability))
print(f"이름: {name}, 국적: {country}, 가능성: {probability}%")


# requests를 불러온다.
# 요청 보낼 url을 작성한다.
# 이름과 함께 요청을 보낸다.
# 응답받은 값을 json 함수를 통해 dict로 변환한다.
# 응답받은 결과의 형태를 확인하고, 
# 첫번째 결과물에서 국가명과 확률을 뽑는다.
# 확률은 소수로 변경해서 퍼센테이지 형태로 변환한다.
    # 곱셈은 *를 사용하시면 됩니다.
# round(): 소수점 반올림 함수