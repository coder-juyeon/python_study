import openpyxl
import requests
from bs4 import BeautifulSoup

fpath = r'C:\startcoding\proejct\01_네이버_주식현재가_크롤링\data.xlsx'
codes = [
    '005930',
    '000660',
    '035720'
]
row = 2

# 1) 엑셀 불러오기
wb = openpyxl.load_workbook(fpath)

# 2) 시트 선택하기
# wb.active : 현재 활성화된 시트 선택
ws = wb['주식']

# 3) 데이터추출

for code in codes:
    reponse = requests.get(f'https://finance.naver.com/item/sise.naver?code={code}')
    html = reponse.text
    soup = BeautifulSoup(html, 'html.parser')
    price = soup.select_one('#_nowVal').text

    # 4) 데이터 수정하기
    ws[f'B{row}'] = price
    row += 1

    # 5) 데이터 저장하기
    wb.save(fpath)







