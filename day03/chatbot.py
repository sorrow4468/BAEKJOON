# requests 불러오기
import requests
from pprint import pprint
# 봇 토큰 변수에 담기
TOKEN = "1881956424:AAG_5YKc3QYA8EhHmPOau_kLfxlEzpdNmrs"
# 요청 통합 URL 변수에 담기
url = f"https://api.telegram.org/bot{TOKEN}"


# 내 챗봇에 메시지 보낸 사람 정보 알아내기 (getUpdates)
get_updates_url = f"{url}/getUpdates"
response = requests.get(get_updates_url).json()
# 그 사람이 보낸 메시지와, 그 사람의 chat_id알아내기
chat_id = (response['result'][0]['message']['from']['id'])
text = (response['result'][0]['message']['text'])


# 메시지 보낸 사람에게
# 그 사람이 보낸 메시지 다시 돌려보내기
# sendMessage method의 필수 params인 chat_id와 text를 넣는다.
send_message_url = f"{url}/sendMessage?chat_id={chat_id}&text={text}"
print(send_message_url)
requests.get(send_message_url)
