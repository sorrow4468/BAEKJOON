import requests
from bs4 import BeautifulSoup

KEY = "yFKV%2BECvAWDL2FspF6wVihm6%2FhemFqTsl9lcic0BCfp1fp2QUVc%2BexlgQ%2BHPsSLDTqkuYP3e%2BNYXPTWhkyvnWw%3D%3D"
station_number = 1
url = f"http://apis.data.go.kr/B552584/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty?serviceKey={KEY}&returnType=json&numOfRows=100&pageNo=1&sidoName=%EB%B6%80%EC%82%B0&ver=1.0"
data = requests.get(url).json()
dust = int(data["response"]["body"]["items"][station_number]["pm10Value"])
station = str(data["response"]["body"]["items"][station_number]["stationName"])
nongdo = ""
if dust > 150:
    nongdo = "매우 나쁨"
elif 80 < dust <= 150:
    nongdo = "나쁨"
elif 30 < dust <= 80:
    nongdo = "보통"
else : 
    nongdo = "좋음"

print(f"{station}의 미세먼지 농도는 {nongdo}입니다.")
