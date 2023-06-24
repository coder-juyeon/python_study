import requests
from bs4 import BeautifulSoup
import pyautogui
import json

input_query = pyautogui.prompt('검색어를 입력해주세요: ')
print(f'input_query: {input_query}')

response = requests.get(f"https://search.naver.com/search.naver?where=news&sm=tab_jum&query={input_query}")
html = response.text
soup = BeautifulSoup(html, 'html.parser')
links = soup.select(".news_tit") # 결과는 리스트
result = []

for link in links:
    title = link.text
    url = link.attrs['href']
    data = {
        'title': title,
        'url': url
    }
    result.append(data)

json_data = json.dumps(result, ensure_ascii=False)
print(json_data)