# setWebHook 요청 보내야 한다.
import requests

#token, url, ngrok url
TOKEN = "1881956424:AAG_5YKc3QYA8EhHmPOau_kLfxlEzpdNmrs"
# 요청 통합 URL 변수에 담기
url = f"https://api.telegram.org/bot{TOKEN}"
ngrok_url = "https://fb310ae62aee.ngrok.io"    
python_anywhere = "https://sorrow4468.pythonanywhere.com"
set_webhook_url = f"{url}/setWebhook?url={python_anywhere}/telegram"
# telegram이 내 ngrok/telegram 으로 요청을 보내고, 200 응답받아간다.
response = requests.get(set_webhook_url)
print(response.text)
