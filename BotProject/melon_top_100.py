import requests
from bs4 import BeautifulSoup
import openpyxl
import json

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import csv

import time
import pyautogui
import pyperclip

import discord
from discord.ext import commands

#크롬 드라이버 자동 업데이트
from webdriver_manager.chrome import ChromeDriverManager

intents = discord.Intents.all()
intents.typing = False  # typing 이벤트 비활성화
intents.presences = False  # presence 이벤트 비활성화
intents.message_content = True #v2

app = commands.Bot(command_prefix='/', intents=intents)

#브라우저 꺼짐 방지
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

#불필요한 에러 메세지 없애기
chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)


# 웹페이지 해당 주소 이름
driver.implicitly_wait(3) # 웹페이지가 로딩 될때까지 5초를 기다린다.
driver.maximize_window() # 화면 최대화

driver.get("https://www.melon.com/chart/")

#제목 가져오기
music_infos = driver.find_elements(By.CSS_SELECTOR, ".lst50")
result = []

@app.event
async def on_ready():
    print('Done')
    await app.change_presence(status=discord.Status.online, activity=None)

@app.command()
async def top100(ctx):
    for idx, info in enumerate(music_infos, start=1):
        title = info.find_element(By.CSS_SELECTOR, ".rank01 span a").text
        
        # 딕셔너리에 제목과 순위 저장
        music_info = {"rank": idx, "title": title}
        
        # 딕셔너리를 result 리스트에 추가
        result.append(music_info)
    await ctx.send(result)

app.run('MTEyMTMxNjQ5ODY3MDEwODcwMw.GiHIj0.rg9pgAAcGz3PjCA7qajeYBK1fdJM_nX-Gy2p6s')