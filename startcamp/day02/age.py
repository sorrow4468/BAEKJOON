import requests

name = "jeongwon"
url = f"https://api.agify.io/?name={name}"
response = requests.get(url).text
print(type(response))
response = requests.get(url).json()
print(type(response))

# name의 나이는 age입니다.
name = response["name"]
age = response["age"]
print(f"{name}의 나이는 {age}살입니다.")

