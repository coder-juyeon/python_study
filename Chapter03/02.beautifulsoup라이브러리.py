import requests
from bs4 import BeautifulSoup

reponse = requests.get("https://www.naver.com/")
soup = BeautifulSoup(reponse.content, 'html.parser')
word = soup.select('div.ly_atcmp')

print(word)