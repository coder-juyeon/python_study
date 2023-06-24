import requests
from bs4 import BeautifulSoup
import pyautogui

input_query = pyautogui.prompt('검색어를 입력해주세요')
lastPageNum = pyautogui.prompt('마지막 페이지를 입력해주세요')
pageNum = 1

for i in range(1,int(lastPageNum) * 10,10):
    print(f'============={pageNum}페이지 입니다.=============')
    response = requests.get(f"https://search.naver.com/search.naver?where=news&sm=tab_jum&query={input_query}&start={i}")
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    links = soup.select(".news_tit") # 결과는 리스트
    for link in links:
        title = link.text
        url = link.attrs['href']
        print(title, url)
    pageNum += 1