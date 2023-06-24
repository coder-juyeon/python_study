import requests
from bs4 import BeautifulSoup
import pyautogui
import json
from flask import Flask


response = requests.get("https://www.saramin.co.kr/zf_user/help/help-word/main")
html = response.text
soup = BeautifulSoup(html, 'html.parser')
links = soup.select(".question") # 결과는 리스트
result = []

for link in links:
    title = link.text
    data = {
        'title': title,
    }
    result.append(data)

json_data = json.dumps(result, ensure_ascii=False)
print(json_data)

""" app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/json')
def json():
    return json_data


if __name__ == '__main__':
    # 애플리케이션 실행
    app.run() """