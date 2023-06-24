import requests
from bs4 import BeautifulSoup
import openpyxl
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import csv

#크롬 드라이버 자동 업데이트
from webdriver_manager.chrome import ChromeDriverManager

import time
import pyautogui
import pyperclip

import discord
from discord.ext import commands

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

@app.event
async def on_ready():
    print('Done')
    await app.change_presence(status=discord.Status.online, activity=None)



#웹페이지 해당 주소이동



#2. 사림인
@app.command()
async def 내놔(ctx): 
    try:
        driver.implicitly_wait(5) #웹페이지가 로딩될때까지 5초 기다린다
        driver.maximize_window() #윈도우창 최대화 
        # driver.get("https://www.saramin.co.kr/zf_user/")

        #사림인 검색창
        saraminSearch = driver.find_element(By.CSS_SELECTOR, ".search")
        saraminInput = driver.find_element(By.CSS_SELECTOR, ".key")
        saraminSearchClick = driver.find_element(By.CSS_SELECTOR, "#btn_search_recruit")

        #사림인 검색어 입력
        saraminSearch.click()
        saraminInput.send_keys('웹개발자')
        saraminSearchClick.click()

        saraminInfosMore = driver.find_element(By.CSS_SELECTOR, ".view_more")
        saraminInfosMore.click()


        #사림인 취업 정보 div
        saraminInfos = driver.find_elements(By.CSS_SELECTOR, ".item_recruit")

        for saraminInfo in saraminInfos:
            postingName = saraminInfo.find_element(By.CSS_SELECTOR, ".data_layer > span").text
            companyName = saraminInfo.find_element(By.CSS_SELECTOR, ".track_event").text
            jobDate = saraminInfo.find_element(By.CSS_SELECTOR, ".date").text

            jobCondition = saraminInfo.find_elements(By.CSS_SELECTOR, ".job_condition > span")

            jobLocation = jobCondition[0].text
            jobExperience = jobCondition[1].text
            educationLevel = jobCondition[2].text
            typeOfWork = jobCondition[3].text
            try:
                averageSalary = jobCondition[4].text
            except:
                averageSalary = "표시된 평균연봉 없음"

            saraminLink = saraminInfo.find_element(By.CSS_SELECTOR, ".data_layer").get_attribute('href')
            print(postingName, companyName, jobDate, jobLocation, jobExperience, educationLevel, typeOfWork, averageSalary)
            await ctx.send(f'```취업정보사이트 : 사람인 \n공고제목 : {postingName}\n기업이름 : {companyName}\n모집기간 : {jobDate}\n기업위치 : {jobLocation}\n경력 : {jobExperience}\n학력 : {educationLevel}\n근로형태 : {typeOfWork}\n연봉 : {averageSalary}```\n링크 : {saraminLink}\n--------------------------------------')
    except:
        await ctx.send(f'{today.month}월 {today.day}일 {today.hour}시 {today.minute}분 사람인봇 오류 발생')


app.run('MTEyMTMxNjQ5ODY3MDEwODcwMw.GdkWVN.qjfUjoCOU6YmiZtS_KppTG2fY4Hev3ULEpqcv4')