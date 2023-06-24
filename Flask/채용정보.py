import requests
from bs4 import BeautifulSoup
import pyautogui
import json
from flask import Flask

input_query = pyautogui.prompt('검색어를 입력해주세요: ')
print(f'input_query: {input_query}')

response = requests.get(f"https://www.saramin.co.kr/zf_user/jobs/list/domestic?loc_mcd=101000&searchType=search&searchword={input_query}&exp_cd=1")
html = response.text
soup = BeautifulSoup(html, 'html.parser')
links = soup.select(".str_tit") # 결과는 리스트
print(f'links: {links}')
result = []

for link in links:
    title = link.text
    print(f'title: {title}')
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