from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/ssafy")
def ssafy():
    return render_template("ssafy.html")

TOKEN = "1881956424:AAG_5YKc3QYA8EhHmPOau_kLfxlEzpdNmrs"
url = f"https://api.telegram.org/bot{TOKEN}"

@app.route("/write")
def write():
    return render_template("write.html")

@app.route("/send")
def send():
    message = request.args.get("message")
    chat_id = 1829024432
    send_message_url = f"{url}/sendMessage?chat_id={chat_id}&text={message}"
    requests.get(send_message_url)
    return render_template("send.html")

@app.route("/telegram", methods = ["POST"])
def telegram():
    response = request.get_json()
    chat_id = response['message']['from']['id']
    text = response['message']['text']

    if text == "누구야?":
        text = "저는 이정원님의 챗봇입니다."
    elif text == "미세먼지":
        KEY = "yFKV%2BECvAWDL2FspF6wVihm6%2FhemFqTsl9lcic0BCfp1fp2QUVc%2BexlgQ%2BHPsSLDTqkuYP3e%2BNYXPTWhkyvnWw%3D%3D"
        station_number = 1
        dust_url = f"http://apis.data.go.kr/B552584/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty?serviceKey={KEY}&returnType=json&numOfRows=100&pageNo=1&sidoName=%EB%B6%80%EC%82%B0&ver=1.0"
        data = requests.get(dust_url).json()
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
        text = f"{station}의 미세먼지 농도는 {nongdo}입니다."

    send_message_url = f'{url}/sendMessage?chat_id={chat_id}&text={text}'
    requests.get(send_message_url)
    return "", 200









if __name__ == "__main__":
    app.run(debug = True)