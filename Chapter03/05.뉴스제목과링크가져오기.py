import requests
from bs4 import BeautifulSoup
import pyautogui

input_query = pyautogui.prompt('검색어를 입력해주세요: ')
print(f'input_query: {input_query}')

response = requests.get(f"https://search.naver.com/search.naver?where=news&sm=tab_jum&query={input_query}")
html = response.text
soup = BeautifulSoup(html, 'html.parser')
links = soup.select(".news_tit") # 결과는 리스트
for link in links:
    title = link.text
    url = link.attrs['href']
    print(title, url)